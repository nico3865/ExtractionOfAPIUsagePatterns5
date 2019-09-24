
import json
import gensim
from gensim import matutils
from gensim.models import Word2Vec
# http://kavita-ganesan.com/gensim-word2vec-tutorial-starter-code/#.XFRrJc9KjmE
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer



def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    # CHANGE_OLD
    stems = stem_tokens(tokens, stemmer)
    # /CHANGE_OLD

    # # CHANGE_NEW
    # # don't stem words
    # stems = tokens
    # # /CHANGE_NEW

    return stems

dict_of_questions_and_code = {}
stemmer = PorterStemmer()

def get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False):
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

        for p in data:
            line = p
            # # CHANGE2_OLD
            # rewritten_intent = line["rewritten_intent"]
            # # /CHANGE2_OLD
            # CHANGE2_NEW:
            # since the rewritten intents are just crazy specific regexes ... don't help at all for NLP ...
            rewritten_intent = line["intent"]
            # /CHANGE2_NEW
            if rewritten_intent is None:
                rewritten_intent = line["intent"]
            lowers = rewritten_intent.lower()

            # # # CHANGE1_OLD:
            # # no_punctuation = lowers.translate(string.punctuation)
            # no_punctuation = lowers.translate(str.maketrans('', '', string.punctuation))
            # # # /CHANGE1_OLD:

            # CHANGE1_NEW:
            # TODO REMOVE MORE PUNCT: TICKS AND QUOTES
            import re
            no_punctuation = re.sub(r'[^\w\s]', ' ', lowers)
            #In above code, we are substituting(re.sub) all NON[alphanumeric characters(\w) and spaces(\s)] with empty string.
            #no_punctuation = no_punctuation.translate(str.maketrans('', '', string.punctuation))
            # /CHANGE1_NEW:

            dict_of_questions_and_code[no_punctuation] = line["snippet"]
            # TODO if key already exist, create a duplicate entry with a special character at start -- this can be interesting too.
    return dict_of_questions_and_code


def return_data_as_dict_of_SOquestions_stemmed____to____original_sentences_____for_word2vec_input_format(dict_of_questions_and_code):
    # dict_of___English___to___stemmed_and_tokenized_English = []
    dict_of___English___to___stemmed_and_tokenized_English = {}
    for key in dict_of_questions_and_code.keys():
        stemmed_and_tokenized = tokenize(key)
        if not stemmed_and_tokenized or len(stemmed_and_tokenized) == 0 or stemmed_and_tokenized == [] or None in stemmed_and_tokenized:
            print("sentence is empty after stemming and tokenization ... for sentence --> " + str(key))
        # dict_of___English___to___stemmed_and_tokenized_English.append(stemmed_and_tokenized)
        stemmed_new_key = " ".join(stemmed_and_tokenized)
        dict_of___English___to___stemmed_and_tokenized_English[stemmed_new_key] = key
    return dict_of___English___to___stemmed_and_tokenized_English




def get_weights_for_words_in_sentence(sentence):
    # str = 'this sentence has unseen text such as computer but also king lord juliet'

    # # CHANGE_BUG_OLD:
    # response = tfidf.transform([' '.join(sentence)])
    # # /CHANGE_BUG_OLD:

    # CHANGE_BUG_NEW:
    global tfidf
    response = tfidf.transform([sentence]) # https://stackoverflow.com/questions/20132070/using-sklearns-tfidfvectorizer-transform
    # /CHANGE_BUG_NEW

    positive_func = []
    for word_counter in range(0, len(response.data)):
        tf_idf_word_index = response.indices[word_counter]
        retreived_word = tfidf_vocab_by_id[tf_idf_word_index]
        positive_func.append((retreived_word, response.data[word_counter]))
    # OLD WAY without tf-idf: positive_func = [(word, 1.0) for word in sentence]
    # adjust, using tf idf weights:
    # vector_of_weighted_words_given_sentence_in_correct_weird_format = model[corpus[0]]
    if not positive_func or positive_func is None:
        print("positive_func is empty for sentence --> " + str(sentence)) # TODO: I think this happens and it's ok, but look into it later ...
    return positive_func # found a bug here ... why are these all letters instead of words ??????

def get_mean_for_sentence(positive):
    """
    @param: sentence, as 2D array of "words with their corresponding weight": e.g. [(word, 1.0) for word in sentence_to_be_avgd]
    :return: the weighted average of all words in sentence:
    """
    from numpy import ndarray
    from numpy import array
    from numpy import float32 as REAL
    global model

    all_words, mean = set(), []
    for word, weight in positive:# + negative:
        if isinstance(word, ndarray):
            mean.append(weight * word)
        else:
            try:
                mean.append(weight * model.wv.word_vec(word, use_norm=True))
                if word in model.wv.vocab:
                    all_words.add(model.wv.vocab[word].index)
            except Exception as e:
                print("word not in vocab? word = "+str(word)+" ... --> "+str(e))
                pass
    if not mean:
        #raise ValueError("cannot compute similarity with no input") # I guess we have to replace with empty words.
        mean.append(0.0 * model.wv.word_vec("none", use_norm=True))   # TODO: improve on this dirty fix ...
    sentence_vector_mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)
    return sentence_vector_mean

import hashlib
def hashFor(data):
    # Prepare the project id hash
    hashId = hashlib.md5()
    hashId.update(repr(data).encode('utf-8'))
    return hashId.hexdigest()






# global, every time this function is called it adds to the totals to get the avg at the end ....
sum_of_BLEU_scores = 0
count_of_BLEU_scores = 0
sum_of_BLEU_scores_MATCHEDQUERY = 0
count_of_BLEU_scores_MATCHEDQUERY = 0
def get_BLEU_score_for_2_strings___CONALA_way(reference_answer_as_code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True):

    # if those were set to zero here it would be the BLEU avg for the 5 nearest neighbours only:
    global sum_of_BLEU_scores
    global count_of_BLEU_scores
    global sum_of_BLEU_scores_MATCHEDQUERY
    global count_of_BLEU_scores_MATCHEDQUERY

    # new code to output in correct format for conala tokenization and eval script:
    json.dump([corresponding_code], open('output.json', 'w'), indent=2)
    # TEST, WORKS --> json.dump(["all(x == myList[0] for x in myList)"], open('reference.json', 'w'), indent=2)
    json.dump([reference_answer_as_code], open('reference.json', 'w'), indent=2)  # could be moved out of the loop ... who cares.
    #   python $SDIR/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp results/$setting.test.json
    # from importlib.machinery import SourceFileLoader
    # conala = SourceFileLoader("conala.conala_eval", "/Users/nicolasg-chausseau/conala-baseline/eval/conala_eval.py").load_module()
    # import conala_eval

    # works except for passing the args:
    import conala_eval
    # conala_eval.main("strip_ref_metadata", "input_ref", "conala-corpus/conala-test.json", "input_hyp", "output.json")
    # conala_eval.main("--strip_ref_metadata --input_ref reference.json --input_hyp output.json")
    tuple_bleu_exact = conala_eval.main(["--strip_ref_metadata", "--input_ref", "reference.json", "--input_hyp", "output.json"])
    # print("variable returned from CONALA EVAL BLEU SCORE: "+str(x))
    # print(x)
    if is_BLEU_for_code_evaluation_NOT_matchedQuery:
        sum_of_BLEU_scores += tuple_bleu_exact[0]
        count_of_BLEU_scores += 1
        current_avg_BLEU = sum_of_BLEU_scores / count_of_BLEU_scores
        print("current_avg_BLEU --> "+str(current_avg_BLEU))
    else:
        sum_of_BLEU_scores_MATCHEDQUERY += tuple_bleu_exact[0]
        count_of_BLEU_scores_MATCHEDQUERY += 1
        current_avg_BLEU_MATCHEDQUERY = sum_of_BLEU_scores_MATCHEDQUERY / count_of_BLEU_scores_MATCHEDQUERY
        print("current_avg_BLEU_MATCHEDQUERY --> "+str(current_avg_BLEU_MATCHEDQUERY))

    # file permissions which doesn't work ...
    # os.system("/Users/nicolasg-chausseau/conala-baseline/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp output.json")

    #sys.exit(1)     # output only the first match, best match.


sum_of_BLEU_scores___NLTK_way = 0
count_of_BLEU_scores___NLTK_way = 0
sum_of_BLEU_scores_MATCHEDQUERY___NLTK_way = 0
count_of_BLEU_scores_MATCHEDQUERY___NLTK_way = 0
def get_BLEU_score_for_2_strings___NLTK_way(reference_answer_as_code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True):

    global sum_of_BLEU_scores___NLTK_way
    global count_of_BLEU_scores___NLTK_way
    global sum_of_BLEU_scores_MATCHEDQUERY___NLTK_way
    global count_of_BLEU_scores_MATCHEDQUERY___NLTK_way

    from nltk.translate.bleu_score import sentence_bleu
    reference = reference_answer_as_code.split(" ") # it was already tokenized before ...
    candidate = corresponding_code.split(" ")

    # print('Cumulative 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
    # print('Cumulative 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
    # print('Cumulative 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
    # print('Cumulative 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))

    score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)) # use only unigrams ... bigrams and above almost never occur anyway.
    #print(score)

    if is_BLEU_for_code_evaluation_NOT_matchedQuery:
        sum_of_BLEU_scores___NLTK_way += score
        count_of_BLEU_scores___NLTK_way += 1
        current_avg_BLEU___NLTK_way = sum_of_BLEU_scores___NLTK_way / count_of_BLEU_scores___NLTK_way
        print("current_avg_BLEU___NLTK_way --> "+str(current_avg_BLEU___NLTK_way))
    else:
        sum_of_BLEU_scores_MATCHEDQUERY___NLTK_way += score
        count_of_BLEU_scores_MATCHEDQUERY___NLTK_way += 1
        current_avg_BLEU_MATCHEDQUERY___NLTK_way = sum_of_BLEU_scores_MATCHEDQUERY___NLTK_way / count_of_BLEU_scores_MATCHEDQUERY___NLTK_way
        print("current_avg_BLEU_MATCHEDQUERY___NLTK_way --> "+str(current_avg_BLEU_MATCHEDQUERY___NLTK_way))




def getBleuScoreForSearchQuery(english_query, reference_answer_as_code):

    #sentence_to_be_avgd = gensim.utils.simple_preprocess(s)
    # sentence_to_be_avgd = s.split(" ")

    # sentence_to_be_avgd = tokenize(s)   # old code for parsing one query at a time
    sentence_to_be_avgd = tokenize(english_query)
    if not sentence_to_be_avgd or len(sentence_to_be_avgd) == 0 or sentence_to_be_avgd == [] or None in sentence_to_be_avgd:
        print("sentence_to_be_avgd is empty after stemming and tokenization ... for sentence-query --> " + str(english_query))
    # dict_of___English___to___stemmed_and_tokenized_English.append(stemmed_and_tokenized)
    sentence_to_be_avgd = " ".join(sentence_to_be_avgd)

    positive_query = get_weights_for_words_in_sentence(sentence_to_be_avgd)  # [(word, 1.0) for word in sentence_to_be_avgd]
    # TODO: fix bug: gensim.utils.simple_preprocess(s) removes the word multidimensional from the sentence ... why?
    sentence_vector_mean_QUERY = get_mean_for_sentence(positive_query)


    # For the simple task of finding the nearest neighbors between two sets of data,
    # the unsupervised algorithms within sklearn.neighbors can be used:
    # ... Because the query set matches the training set,
    # the nearest neighbor of each point is the point itself, at a distance of zero.
    from sklearn.neighbors import NearestNeighbors
    import numpy as np
    # X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])   # dummy dataset of vectors
    X = np.array(dataset_of_sentence_vectors_for_KNN)   # real dataset of vectors
    nbrs = NearestNeighbors(n_neighbors=5, leaf_size=1, algorithm='brute').fit(X)
        # ‘ball_tree’ will use BallTree
        # ‘kd_tree’ will use KDTree
        # ‘brute’ will use a brute-force search.
        # ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.
    # distances, indices = nbrs.kneighbors(X)   # on itself ...
    # distances, indices = nbrs.kneighbors([[-1, -0.9]])  # dummy data point
    distances, indices = nbrs.kneighbors([sentence_vector_mean_QUERY], 5)  # real search query vector data point
    print("distances and indices:")
    print(distances)
    print(indices)

    for indices_unwrapped in indices:
        for place in indices_unwrapped:
            try:
                neighbour = X[place]
                # print(neighbour)

                # get original sentence:
                # hashFor(str(sentence_vector_mean_DATAPOINT)
                # best_sentence_match_to_query = hash_of_coordinates_to_original_sentence[str(indices[0])]
                # best_sentence_match_to_query = hash_of_coordinates_to_original_sentence[hashFor(str(neighbour))]
                best_sentence_match_to_query = hash_of_coordinates_to_original_sentence[str(neighbour)]  # it's giving same result exactly as when I use the hash function.

                print("\n")
                print("---new nearest neighbour for same query---")

                print("best_sentence_match_to_query: ")
                print(best_sentence_match_to_query)
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code: ")
                corresponding_original_SOquestion = dict_of_SOquestions_stemmed___to___original_SOquestions[best_sentence_match_to_query]
                corresponding_code = dict_of_questions_and_code[corresponding_original_SOquestion]
                print(corresponding_code)

                #import conala_eval why not found....
                get_BLEU_score_for_2_strings___CONALA_way(reference_answer_as_code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
                get_BLEU_score_for_2_strings___CONALA_way(english_query, corresponding_original_SOquestion, is_BLEU_for_code_evaluation_NOT_matchedQuery=False)
                print("bleu nltk for comparisno: ")
                get_BLEU_score_for_2_strings___NLTK_way(reference_answer_as_code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
                get_BLEU_score_for_2_strings___NLTK_way(english_query, corresponding_original_SOquestion, is_BLEU_for_code_evaluation_NOT_matchedQuery=False)


            except Exception as e:
                print("error retrieving original document")
                print(e)
                pass

dict_of_SOquestions_stemmed___to___original_SOquestions = []
model = gensim.models.Word2Vec()
def train_and_write_word2vec_to_global_var():


    # -- place corpus words in word2vec space, and store in global var ----
    global dict_of_questions_and_code
    global dict_of_SOquestions_stemmed___to___original_SOquestions
    global model

    # # very small, but manually groomed corpus: (but the manually rewritten intents aren't that great actually, confusing stuff for word2vec and tf-idf with placeholderes etc -- raw English is better)
    input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-train.json"
    dict_of_questions_and_code = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False)

    # bigger corpus:
    # input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-mined.jsonl"
    # dict_of_questions_and_code = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=True)
    try:
        code_for_empty_entry = dict_of_questions_and_code[""]
    except:
        print("GOOD -- no empty entry in SOquestions")


    dict_of_SOquestions_stemmed___to___original_SOquestions = return_data_as_dict_of_SOquestions_stemmed____to____original_sentences_____for_word2vec_input_format(dict_of_questions_and_code)
    # try:
    #     code_for_empty_entry = list_of_SOquestions___stemmed_and_tokenized[]
    # except:
    #     print("GOOD -- no empty entry in SOquestions")

    list_of_SOquestions_stemmed = [stemmed_SOquestion.split(" ") for stemmed_SOquestion in dict_of_SOquestions_stemmed___to___original_SOquestions.keys()]

    # build vocabulary and train model
    model = gensim.models.Word2Vec(
        list_of_SOquestions_stemmed, # to test OLD WAY: change this param to dict_of_SOquestions_stemmed___to___original_SOquestions
        size=150,
        window=10,
        min_count=0,
        workers=10)
    model.train(list_of_SOquestions_stemmed, total_examples=len(list_of_SOquestions_stemmed), epochs=10)
    # OLD WAY: model.train(dict_of_SOquestions_stemmed___to___original_SOquestions, total_examples=len(dict_of_SOquestions_stemmed___to___original_SOquestions), epochs=10)

    model.save("word2vec.model")
    # model = Word2Vec.load("word2vec_BIG.model")
    model = Word2Vec.load("word2vec.model")


    try:
        w1 = "boolean"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)

    try:
        w1 = "list"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)


    try:
        w1 = "dictionary"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)

    try:
        w1 = "array"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)


    try:
        w1 = "sort"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)


    try:
        w1 = "pip"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)

    try:
        w1 = "loop"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)

    try:
        w1 = "integer"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)

    try:
        w1 = "dirty"
        print(w1)
        most_similar = model.wv.most_similar(positive=w1)
        print(most_similar)
    except Exception as e:
        print(e)

    # # -- /place corpus words in word2vec space ----






tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfidf_vocab_by_id = {}
def train_and_write_tfidf_to_global_var():

    # ----
    # https://github.com/RaRe-Technologies/gensim/blob/1f357a7c4db27ea9c946dbc6942d82b00815a55e/gensim/models/keyedvectors.py#L510
    # compute the weighted average of all words

    #this can take some time # https://stackoverflow.com/questions/20132070/using-sklearns-tfidfvectorizer-transform
    global tfidf
    global tfidf_vocab_by_id
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    # tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', stop_words='english', vocabulary=vocabulary)
    tfs = tfidf.fit_transform(dict_of_questions_and_code.keys())
    print("vectorizer.get_feature_names() --> "+str(tfidf.get_feature_names()))
    tfidf_vocab_by_id = {} # so we can retrieve words from their ids later ...
    for word, id in tfidf.vocabulary_.items():
        tfidf_vocab_by_id[id] = word



dataset_of_sentence_vectors_for_KNN = []
hash_of_coordinates_to_original_sentence = {}
def build_and_write_KNN_to_global_var():

    # -- cut ---

    # build dataset of sentences for KNN:
    # this btw could be done only once for any dataset, it's a bit long:
    dataset_of_sentence_vectors_for_KNN = []
    hash_of_coordinates_to_original_sentence = {}
    i=0
    for doc_stemmed, doc in dict_of_SOquestions_stemmed___to___original_SOquestions.items():  # , doc
        if not doc_stemmed or doc_stemmed == []:
            print("document has empty question after stemming ... "+str(doc_stemmed))
        i += 1
        positive_doc = get_weights_for_words_in_sentence(doc_stemmed)  # [(word, 1.0) for word in sentence_to_be_avgd]
        if positive_doc is None or 'none' in positive_doc:
            print("if positive_doc is None or 'none' in positive_doc:")
        sentence_vector_mean_DATAPOINT = get_mean_for_sentence(positive_doc)
        dataset_of_sentence_vectors_for_KNN.append(sentence_vector_mean_DATAPOINT) #.tolist() or .todict()
        # consider making the key a string to avoid approx errors when retrieving later:
        # or use another KNN model to retrieve the nearest point ... even if it's exactly spot on the same coordinates:
        # https://stackoverflow.com/questions/7257588/why-cant-i-use-a-list-as-a-dict-key-in-python
        hash_of_coordinates_to_original_sentence[str(sentence_vector_mean_DATAPOINT)] = doc_stemmed  # NO, MY BUG, SOLVED --> the index is so long that it causes a bug where the dict only keeps the last entry, always length 1
        #hash_of_coordinates_to_original_sentence[i] = doc
        #hash_object = hashlib.md5(b'Hello World')
        # hash_of_coordinates_to_original_sentence[hashFor(str(sentence_vector_mean_DATAPOINT))] = doc
        # print("__________ ")
        # print(str(sentence_vector_mean_DATAPOINT))

    # TODO: fix lossy serialization of dataset:
    # # TODO: save these as files, a serialized list and a serialized hash ... and load them instead
    # hash_of_coordinates_to_original_sentence_AS_STRING = json.dumps(hash_of_coordinates_to_original_sentence)
    # text_file = open("hash_of_coordinates_to_their_original_dataset_sentence.txt", "w")
    # text_file.write(hash_of_coordinates_to_original_sentence_AS_STRING)
    # text_file.close()
    # # # load it:
    # # with open('hash_of_coordinates_to_their_original_dataset_sentence.txt') as f:
    # #     dataset_of_sentence_vectors_for_KNN___read_data = f.read()
    # # f.closed
    # # hash_of_coordinates_to_original_sentence = json.loads(dataset_of_sentence_vectors_for_KNN___read_data)
    # # print("hash_of_coordinates_to_their_original_dataset_sentence: ")
    # # print(hash_of_coordinates_to_original_sentence)
    #
    # # TODO: save these as files, a serialized list and a serialized hash ... and load them instead
    # dataset_of_sentence_vectors_for_KNN_AS_STRING = json.dumps(dataset_of_sentence_vectors_for_KNN)
    # text_file = open("dataset_of_sentence_vectors_for_KNN.txt", "w")
    # text_file.write(dataset_of_sentence_vectors_for_KNN_AS_STRING)
    # text_file.close()
    # # # load it:
    # # with open('dataset_of_sentence_vectors_for_KNN.txt') as f:
    # #     dataset_of_sentence_vectors_for_KNN___read_data = f.read()
    # # f.closed
    # # dataset_of_sentence_vectors_for_KNN = json.loads(dataset_of_sentence_vectors_for_KNN___read_data)
    # # print("dataset_of_sentence_vectors_for_KNN: ")
    # # print(dataset_of_sentence_vectors_for_KNN)




def get_BLEU_for_ref_translation_test_set(input_file_REFERENCE):

    # --- cut ----

    # load the reference translations:

    dict_of_questions_and_code_REFERENCE = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file_REFERENCE, is_jsonl_binary_file=False)
    try:
        code_for_empty_entry_REFERENCE = dict_of_questions_and_code_REFERENCE[""]
    except:
        print("GOOD -- no empty entry in SOquestions")


    for SOquestion, code in dict_of_questions_and_code_REFERENCE.items():

        print("------------------------------------evaluating for a new reference: query+code------------------------------------------")

        # # define a search query:
        # # s = "How can I define multidimensional arrays in python"
        # # s = "throw an error window in python in windows"
        # # s = "print variable value without spaces"   # really good matches
        # # s = "beautifulsoup select div elements with an id attribute value ending with sub string in html parsed string soup"
        # # s = "How can I send a signal from a python program?"
        # # s = "Decode Hex String in Python 3"
        # s="check if all elements in a list are identical"               # this one gives such great matches ...
        # # s="Format string dynamically"
        # # s="How to convert a string from CP-1251 to UTF-8?"
        # # s="How I can get rid of None values in dictionary?"
        # # s="Python: how to get the final output of multiple system commands?"
        # # s="splitting and concatenating a string"
        # # s="Finding the intersection between two series in Pandas"
        # # s="Sending http headers with python"
        # # s="Python -Remove Time from Datetime String"
        # # s="How do I split a multi-line string into multiple lines?"
        # # s="How to join mixed list (array) (with integers in it) in Python?"
        # # s="Fastest way to get the first object from a queryset in django?"
        #
        # print("query is --> "+s)
        print("query is --> "+str(SOquestion))

        print("the BLEU scores below are for the following reference translation: ")
        print(code)

        getBleuScoreForSearchQuery(SOquestion, code)

        print()





if __name__ == "__main__":
    train_and_write_word2vec_to_global_var()
    train_and_write_tfidf_to_global_var()
    build_and_write_KNN_to_global_var()

    input_file_REFERENCE = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-test.json"
    get_BLEU_for_ref_translation_test_set(input_file_REFERENCE)

