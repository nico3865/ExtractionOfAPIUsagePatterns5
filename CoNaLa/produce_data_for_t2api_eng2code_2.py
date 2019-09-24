
import json
import sys

import gensim
from gensim import matutils
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
# http://kavita-ganesan.com/gensim-word2vec-tutorial-starter-code/#.XFRrJc9KjmE

import nltk
import string
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer








# # tokenizing into words:
# def word_tokenize(data):
#     tokenized_words = nltk.word_tokenize(data)
#     #print(tokenized_words)
#     return tokenized_words




IS_USING_SMALL_ANNOTATED_CORPUS_ONLY = False #True #False

IS_IN_REVERSE___IE_CODE_2_ENGLISH = True #True
IS_REMOVE_PUNCTUATION_IN_ENGLISH_INTENTS = False #False #True # False # remove punct only for English2Code

NUM_NEIGHBOURS_TO_OUTPUT = 1 # 20


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
        tokens = nltk.word_tokenize(text.lower())
        # fix issue "nltk tokenizeer doesnt split on dots for some reason ... "
        tokens_cleaned_separated_on_dots = []
        for token in tokens:
            token_split = token.split(".")
            if len(token_split) > 1:
                #token_split_join = " . ".join(token_split)
                for new_token in token_split:
                    tokens_cleaned_separated_on_dots.append(new_token)
            else:
                tokens_cleaned_separated_on_dots.append(token)
        tokens = tokens_cleaned_separated_on_dots
        stems = tokens
    else:
        tokens = nltk.word_tokenize(text)

        # CHANGE_OLD
        stems = stem_tokens(tokens, stemmer)
        # /CHANGE_OLD

        # # CHANGE_NEW
        # # don't stem words
        # stems = tokens
        # # /CHANGE_NEW

    return stems

dict_of_questions_and_code_TRAIN = {}
stemmer = PorterStemmer()

stems_1 = stem_tokens(["multidimensional"], stemmer)
print(stems_1)
stems_2 = stem_tokens(stems_1, stemmer)
print(stems_2)
stems_3 = stem_tokens(stems_2, stemmer)
print(stems_3)
# sys.exit()

# def stem_tokens(tokens, stemmer):
#     stemmed = []
#     for item in tokens:
#         stemmed.append(stemmer.stem(item))
#     return stemmed
#
# def tokenize(text):
#     tokens = nltk.word_tokenize(text)
#     stems = stem_tokens(tokens, stemmer)
#     return stems

def get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False, isForReferenceFile=False):
    # dict_of_questions_and_code = {}
    import collections
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

            if IS_REMOVE_PUNCTUATION_IN_ENGLISH_INTENTS:
                # # # CHANGE1_NEW:
                # # # --FINE, dont see any anymore TODO REMOVE MORE PUNCT: TICKS AND QUOTES
                import re
                no_punctuation = re.sub(r'[^\w\s]', ' ', lowers)
                # # #In above code, we are substituting(re.sub) all NON[alphanumeric characters(\w) and spaces(\s)] with empty string.
                # # #no_punctuation = no_punctuation.translate(str.maketrans('', '', string.punctuation))
                # # # /CHANGE1_NEW:
            else:
                # # CHANGE1_NEW2: no punctuation at all ... doesn't really improve anything.
                no_punctuation = lowers
                # # /CHANGE1_NEW2:

            # -- DONE, used spaces: TODO if key already exist, create a duplicate entry with a special character at start -- this can be interesting too.
            # print()

            # ----- jun 2019: -------
            no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION = no_punctuation + ""
            if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
                while no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION in dict_of_questions_and_code.values():
                    no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION = no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION + " "
                #dict_of_questions_and_code[no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION] = line["snippet"].lower() # old way before noticing collisions on values when they become keys, when reversing the reference test set dict

                # --DONE TODO: redo these t2api input files, but this time running with tokenization ... and then join on spaes
                # because it's getting ugly code tokens in the java code and params.txt file ... tokens are like [[hasattr(
                line_snippet = tokenize(line["snippet"])
                line_snippet = " ".join(line_snippet)


                line_snippet_lower = line_snippet.lower() #line["snippet"].lower()
                line_snippet_lower_WITH_SPACES_AT_END_FOR_DIFFERENTIATION = line_snippet_lower + ""
                while line_snippet_lower_WITH_SPACES_AT_END_FOR_DIFFERENTIATION in dict_of_questions_and_code.keys():
                    line_snippet_lower_WITH_SPACES_AT_END_FOR_DIFFERENTIATION = line_snippet_lower_WITH_SPACES_AT_END_FOR_DIFFERENTIATION + " "

                # old way: now do it directly in here instead of reversing the dict after the fact --> dict_of_questions_and_code[no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION] = line_snippet_lower_WITH_SPACES_AT_END_FOR_DIFFERENTIATION
                dict_of_questions_and_code[line_snippet_lower_WITH_SPACES_AT_END_FOR_DIFFERENTIATION] = no_punctuation_WITH_SPACES_AT_END_FOR_DIFFERENTIATION
            else:
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

            # TODO: append to new file directly in the loop, instead of keeping everything in RAM...
            # as done here: https://www.tutorialspoint.com/How-to-merge-multiple-files-into-a-new-file-using-Python


        print("len(dict_of_questions_and_code)"+str(len(dict_of_questions_and_code)))

    return dict_of_questions_and_code


print()
# ----------------------------------------------------- pick a corpus ---------------------------------------------------------
print()

if IS_USING_SMALL_ANNOTATED_CORPUS_ONLY:
    # very small, but manually groomed corpus: (but the manually rewritten intents aren't that great actually, confusing stuff for word2vec and tf-idf with placeholderes etc -- raw English is better)
    input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-train.json"
    dict_of_questions_and_code_TRAIN = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False)
else:
    # bigger corpus: # does contain the smaller corpus as a subset
    input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-mined.jsonl"
    dict_of_questions_and_code_TRAIN = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=True)

# for key, value in dict_of_questions_and_code_TRAIN.items():
#     print(key +" --> "+value)
# sys.exit()

print()
# ----------------------------------------------------- /pick a corpus ---------------------------------------------------------
print()


# write to files for t2api berkeley aligner format: just two aligned text files -- line per line parallele corpus in two files
# for key, value in dict_of_questions_and_code_TRAIN:


with open('train.ts', 'w') as transl_answers_file:
    #json.dump(dict_of_questions_and_code_TRAIN.keys, outfile_results_conala_eval)
    #transl_answers_file.write(dict_of_questions_and_code_TRAIN.values().totsring())
    for sentence in dict_of_questions_and_code_TRAIN.values():
        sentence = sentence.replace('\n', ' ').replace('\r', '')
        transl_answers_file.write(sentence+"\n")
with open('train.cd', 'w') as transl_input_file:
    #json.dump(dict_of_questions_and_code_TRAIN.values, transl_input_file)
    #transl_input_file.write(dict_of_questions_and_code_TRAIN.keys().tostring())
    for sentence in dict_of_questions_and_code_TRAIN.keys():
        sentence = sentence.replace('\n', ' ').replace('\r', '')
        transl_input_file.write(sentence+"\n")




# now again for test set:
test_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-test.json"
dict_of_questions_and_code_TEST = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(test_file, is_jsonl_binary_file=False)

with open('tune.ts', 'w') as transl_answers_file:
    #json.dump(dict_of_questions_and_code_TRAIN.keys, outfile_results_conala_eval)
    #transl_answers_file.write(dict_of_questions_and_code_TRAIN.values().totsring())
    for sentence in dict_of_questions_and_code_TEST.values():
        sentence = sentence.replace('\n', ' ').replace('\r', '')
        transl_answers_file.write(sentence+"\n")
with open('tune.cd', 'w') as transl_input_file:
    #json.dump(dict_of_questions_and_code_TRAIN.values, transl_input_file)
    #transl_input_file.write(dict_of_questions_and_code_TRAIN.keys().tostring())
    for sentence in dict_of_questions_and_code_TEST.keys():
        sentence = sentence.replace('\n', ' ').replace('\r', '')
        transl_input_file.write(sentence+"\n")
