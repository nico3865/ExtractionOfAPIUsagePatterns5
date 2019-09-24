import json 
import subprocess
import re
import collections
import os
import sys

from rouge.rouge import rouge_n_sentence_level


# load conala-test.json

# for each, get the bleu
# for each get the f1 score

# avg them




# 

def get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False, isForReferenceFile=False):
    # dict_of_questions_and_code = {}
    # import collections
    dict_of_questions_and_code = collections.OrderedDict()

    with open(input_file) as json_file:

        # for json files:
        if not is_jsonl_binary_file:
            data = json.load(json_file)
        # for jsonl files:
        else:
            data = [json.loads(jline) for jline in json_file.readlines()] # weird ... gives an error but only in run mode, not in debug more ...
            # data = []
            # for jline in json_file.readlines():
            #     try:
            #         entry = json.loads(jline)
            #         data.append(entry)
            #     except Exception as e:
            #         print(e)

        all_english_lines = []

        print("len(data)"+str(len(data)))

        for p in data:
            line = p
            # CHANGE2_OLD
            rewritten_intent = None
            if "rewritten_intent" in line:
                rewritten_intent = line["rewritten_intent"]
            # /CHANGE2_OLD

            # # CHANGE2_NEW:
            # # since the rewritten intents are just crazy specific regexes ... don't help at all for NLP ...
            # rewritten_intent = line["intent"]
            # # /CHANGE2_NEW

            if rewritten_intent is None:
                rewritten_intent = line["intent"]
    # for subdir, dirs, files in os.walk(path):
    #     for file in files:
    #         file_path = subdir + os.path.sep + file
    #         shakes = open(file_path, 'r')
    #         text = shakes.read()
            lowers = rewritten_intent.lower()

            # # # CHANGE1_OLD:
            # # no_punctuation = lowers.translate(string.punctuation)
            # no_punctuation = lowers.translate(str.maketrans('', '', string.punctuation))
            # # # /CHANGE1_OLD:

            # # # CHANGE1_NEW:
            # # # --FINE, dont see any anymore TODO REMOVE MORE PUNCT: TICKS AND QUOTES
            # import re
            no_punctuation = re.sub(r'[^\w\s]', ' ', lowers)
            # # #In above code, we are substituting(re.sub) all NON[alphanumeric characters(\w) and spaces(\s)] with empty string.
            # # #no_punctuation = no_punctuation.translate(str.maketrans('', '', string.punctuation))
            # # # /CHANGE1_NEW:

            # # # CHANGE1_NEW2: no punctuation at all ... doesn't realy improve anything.
            # no_punctuation = lowers
            # # # /CHANGE1_NEW2:

            # -- DONE, used spaces: TODO if key already exist, create a duplicate entry with a special character at start -- this can be interesting too.
            # print()

            # ----- jun 2019: -------
            no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION = no_punctuation + ""
            while no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION in dict_of_questions_and_code.keys():
                no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION = no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION + " "
            dict_of_questions_and_code[no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION] = line["snippet"]

            # if isForReferenceFile == True:
            #     if no_punctuation in dict_of_questions_and_code.keys():
            #         print("ERROR, ABORTING --> no_punctuation in dict_of_questions_and_code.keys()")
            #         print("no_punctuation --> "+str(no_punctuation))
            #         print("dict_of_questions_and_code.keys() --> "+str(dict_of_questions_and_code.keys()))
            #         sys.exit()
            #     else:
            #         dict_of_questions_and_code[no_punctuation] = line["snippet"]
            # else:
            #     if no_punctuation in dict_of_questions_and_code.keys():
            #         print("ERROR, ABORTING --> no_punctuation in dict_of_questions_and_code.keys()")
            #         print("no_punctuation --> "+str(no_punctuation))
            #         print("dict_of_questions_and_code.keys() --> "+str(dict_of_questions_and_code.keys()))
            #         sys.exit()
            #     else:
            #         dict_of_questions_and_code[no_punctuation] = line["snippet"]

        print("len(dict_of_questions_and_code)"+str(len(dict_of_questions_and_code)))

    return dict_of_questions_and_code






# load conala-test 
input_file_REFERENCE_conala = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-test.json"
dict_of_questions_and_code_REFERENCE = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file_REFERENCE_conala, is_jsonl_binary_file=False, isForReferenceFile=True)

# load conala-train:
input_file_TRAIN_conala = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-train.json"
dict_of_questions_and_code_TRAIN = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file_TRAIN_conala, is_jsonl_binary_file=False)

# keep track of max scores to avg them:
SUM_OF_max_bleu_for_question = 0
COUNTER_OF_max_bleu_for_question = 0
counter_of_errors_during_BLEU_calculation = 0
COUNTER_OF_max_F1_for_question = 0
SUM_OF_max_F1_for_question = 0
counter_of_errors_during_F1_calculation = 0

# for each question in conala-test:
for key, val in dict_of_questions_and_code_REFERENCE.items():

    # # ----------------- get ceiling F1s (done directly in conala's bleu.py) --------------------
    # recall, precision, rouge = rouge_n_sentence_level(
    #     ['I','am','not','coding','now'],
    #     ['I','am','coding','now'],
    #     1
    # )
    # print(' ROUGE-4-R', recall)
    # print(' ROUGE-4-P', precision)
    # print(' ROUGE-4-F', rouge)
    # sys.exit()
    # # ----------------- /get ceiling F1s --------------------


    # -------------- get ceiling BLEUs -----------------
	# generate a file with 5000 times that question
    ceiling_temp_file_name = '/Users/nicolasg-chausseau/conala-baseline/conala-corpus/FACEBOOK_ENG_2_CODE_CEILING.test.json'
    # clear it at every new test set question:
    open(ceiling_temp_file_name, 'w').close()
    # start writing to it:
    outfile_results_conala_eval = open(ceiling_temp_file_name, 'a+')
    outfile_results_conala_eval.write("[\n")
    for i in range(0, len(dict_of_questions_and_code_TRAIN)):
        outfile_results_conala_eval.write('"')
        outfile_results_conala_eval.write(val)
        outfile_results_conala_eval.write('"')
        if i != len(dict_of_questions_and_code_TRAIN) - 1:
            outfile_results_conala_eval.write(',\n')
    outfile_results_conala_eval.write("\n]")
    outfile_results_conala_eval.close()

    # collect the output,
    # 	that says the one that has the max BLEU
    #	that outputs the actual line of code
    # add max-BLEU to sumBLEU
    # get the max F1 score
    # 	also get the corresponding best-F1 answer from training set
    # add F1 to sumF1
    # avgOfMaxBLEUs
    # avgOfMaxF1

    # call the BLEU script:
    # python "/Users/nicolasg-chausseau/conala-baseline/eval/conala_eval.py" --strip_ref_metadata --input_ref conala-corpus/conala-train.json --input_hyp '/Users/nicolasg-chausseau/conala-baseline/conala-corpus/FACEBOOK_ENG_2_CODE_CEILING.test.json'
    # nicolass-MacBook-Pro-2:conala-baseline nicolasg-chausseau$ sudo bash conala_baseline_EVAL_ONLY_FOR_FACEBOOK.sh
    # hello
    # bleu:25.84
    # exact:7.14
    # nicolass-MacBook-Pro-2:conala-baseline nicolasg-chausseau$

    # cmd = 'wc -l my_text_file.txt > out_file.txt'
    # os.system(cmd)

    out = subprocess.Popen(
        ['bash', '/Users/nicolasg-chausseau/conala-baseline/conala_baseline_EVAL_ONLY_FOR_FACEBOOK.sh'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        #shell=True
    )
    stdout,stderr = out.communicate()
    # print(stdout)
    max_bleu_for_question = stdout.decode('utf-8').split("\n")[1]
    print(max_bleu_for_question)
    max_F1_for_question = stdout.decode('utf-8').split("\n")[3]
    print(max_F1_for_question)
    print("-----")
    #print()
    #print(stderr)
    #print("----------------------------------------------------------------------------------")
    #print(stdout.split(" ")[1])
    COUNTER_OF_max_bleu_for_question += 1
    try:
        SUM_OF_max_bleu_for_question += float(max_bleu_for_question)
    except:
        counter_of_errors_during_BLEU_calculation += 1
        pass

    COUNTER_OF_max_F1_for_question += 1
    try:
        SUM_OF_max_F1_for_question += float(max_F1_for_question)
    except:
        counter_of_errors_during_F1_calculation += 1
        pass
    # -------------- /get ceiling BLEUs -----------------







if COUNTER_OF_max_bleu_for_question != len(dict_of_questions_and_code_REFERENCE):
    print("error, COUNTER_OF_max_bleu_for_question != len(dict_of_questions_and_code_REFERENCE)")
avg_MAX_BLEU = SUM_OF_max_bleu_for_question / COUNTER_OF_max_bleu_for_question
print(avg_MAX_BLEU)
print("counter_of_errors_during_BLEU_calculation --> "+str(counter_of_errors_during_BLEU_calculation))
print("COUNTER_OF_max_bleu_for_question --> "+str(COUNTER_OF_max_bleu_for_question))
print("len(dict_of_questions_and_code_TRAIN): --> "+str(len(dict_of_questions_and_code_TRAIN)))


if COUNTER_OF_max_F1_for_question != len(dict_of_questions_and_code_REFERENCE):
    print("error, COUNTER_OF_max_F1_for_question != len(dict_of_questions_and_code_REFERENCE)")
avg_MAX_F1 = SUM_OF_max_F1_for_question / COUNTER_OF_max_F1_for_question
print(avg_MAX_F1)
print("counter_of_errors_during_F1_calculation --> "+str(counter_of_errors_during_F1_calculation))
print("COUNTER_OF_max_F1_for_question --> "+str(COUNTER_OF_max_F1_for_question))
print("len(dict_of_questions_and_code_TRAIN): --> "+str(len(dict_of_questions_and_code_TRAIN)))







# 1- use only Kmeans.predict
# 2- try to answer the question: how well separated are the clusters? Are they real clusters, significant? or they are not real clusters?
# 3- if you have real clusters in your users, then run a correlation between each cluster, and each known user-type, even if the data is not high-certainty data.
# 4- answer the following question: what do the clusters mean exactly?
# 	during the netflix "collaborative filtering challenge", the winning team identified the "meaning" of each axis in the PCA output:
# 		e.g. the first axis was: masculinity of movie / user
# 		e.g. the second axis was comedy versus drama aspect of movie / user
# 		e.g. the third axis was
# 		.... look for cluster meaning, or PCA axis meaning.
# 		... the way to do that is to manually inspect the data or run correlations with known user categories.
# 			correlations or categorical correlations goodness-of-fit or chi-square
# 			t-test between two distributions
# 			chi-square test between smoking and gender ... is this correlated?
# 			what about running a sample correlation between each feature, and each known user-type class
# 			and then repeat but using combinations of features -- that would be like training a decision tree but instead of classifying for KMEANS labels, you would train it to classify the known user-type labels.
# 0- are users doing all those things: collecting cars, racing, and simulation ... ? or some users only do one of those games significantly more than the other games.
# 	k-gram
# 	n-gram
# 	... in other words you're trying to determine if users switch to one type of game to the other?'
# 	are features predictive at all?
# 		run PCA and check how predictive the first 5 components are
# 		just check if users really play one game more than the other ...
# 0.1- add gender to your data, and any other predictive feature:
# 	age,
# 	gender,
# 	speed of clicking,
# 	best score at each game-category,
# 	avg score at each game-category,
# 	"clicking features"
# 		do they click really fast, or they click really relaxed and slow
# 		how fast are they sliding the window
# 		how far are they sliding the window
# 	----
# 	"user personality features"
# 	"game data features"
# 	// "facebook data features"

