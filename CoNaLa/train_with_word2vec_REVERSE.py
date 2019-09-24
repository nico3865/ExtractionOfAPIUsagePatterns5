
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




IS_USING_SMALL_ANNOTATED_CORPUS_ONLY = True #False #False

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
                line_snippet_lower = line["snippet"].lower()
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


print()
# ----------------------------------------------------- invert data if doing Code2English ---------------------------------------------------------
print()

# old, now just reverse it right away as we build it.
# if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
#     dict_of_questions_and_code_TRAIN = {v: k for k, v in dict_of_questions_and_code_TRAIN.items()}

print()
# ----------------------------------------------------- /invert data if doing Code2English ---------------------------------------------------------
print()

try:
    code_for_empty_entry = dict_of_questions_and_code_TRAIN[""]
except:
    print("GOOD -- no empty string key in SOquestions")

# # https://stackoverflow.com/questions/34318524/recuperating-original-term-doc-id-in-sci-kit-tfidf-vectorizer
# idTracker = {}
# idCounter = 1
# for question, code in dict_of_questions_and_code.iteritems():
#     corpus.append(question)
#     idTracker[idCounter] = id
#     idCounter +=1


def return_data_as_dict_of_SOquestions_stemmed____to____original_sentences_____for_word2vec_input_format(dict_of_questions_and_code_2):
    # dict_of___English___to___stemmed_and_tokenized_English = []
    dict_of___English___to___stemmed_and_tokenized_English = {}
    for key in dict_of_questions_and_code_2.keys():
        stemmed_and_tokenized = tokenize(key)
        #stemmed_and_tokenized = key.split(" ")
        #stemmed_and_tokenized = nltk.word_tokenize(key)
        if not stemmed_and_tokenized or len(stemmed_and_tokenized) == 0 or stemmed_and_tokenized == [] or None in stemmed_and_tokenized:
            print("\n")
            print("sentence is empty after stemming and tokenization ... for sentence --> " + str(key))
            sys.exit()
        # dict_of___English___to___stemmed_and_tokenized_English.append(stemmed_and_tokenized)
        stemmed_new_key = " ".join(stemmed_and_tokenized)
        dict_of___English___to___stemmed_and_tokenized_English[stemmed_new_key] = key
    return dict_of___English___to___stemmed_and_tokenized_English



# for json files:
# def read_input(input_file):
#     with open(input_file) as json_file:
#         data = json.load(json_file)
#         all_english_lines = []
#         for p in data:
#             line = p
#             rewritten_intent = line["rewritten_intent"]
#             # r_i_tokenized = word_tokenize(rewritten_intent)
#
#             print()
#
#             # do some pre-processing and return list of words for each review
#             # text
#             #yield gensim.utils.simple_preprocess(line)
#             try:
#                 # x = gensim.utils.simple_preprocess(rewritten_intent)
#                 # -WTVER for now ignore this problem TODO: check if it splits package.class.function correctly at the dots.
#                 # --FIXED, it's just that I was training tf-idf on the non-stemmed questions ... and it wans't finding entries in its vocab --> TODO: find another tokenizer, this one from gensim removes words like "multidimensional" ...
#                 x = rewritten_intent.split(" ")
#                 all_english_lines.append(x)
#                 # NOT TESTED REALLY:
#                 # lowers = rewritten_intent.lower()
#                 # no_punctuation = lowers.translate(string.punctuation) #lowers.translate(None, string.punctuation)
#                 # # dict_of_questions_and_code[file] = no_punctuation
#                 # stemmed_and_tokenized = tokenize(no_punctuation)
#                 # all_english_lines.append(stemmed_and_tokenized)
#
#             except Exception as e:
#                 continue
#             print()
#
#             # # from gensim.models import FastText
#             # # # [...]
#             # # sentences = SentencesIterator(tokens_generator)
#             # # model = FastText(sentences)
#     return all_english_lines





#
# # a bit bigger:
# input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-mined.jsonl"
#
# # for jsonl files:
# def read_input(input_file):
#     with open(input_file) as json_file:
#         result = [json.loads(jline) for jline in json_file.readlines()]
#         all_english_lines = []
#         for p in result:
#             line = p
#             rewritten_intent = line["intent"]
#             # r_i_tokenized = word_tokenize(rewritten_intent)
#
#             #print()
#
#             # do some pre-processing and return list of words for each review
#             # text
#             #yield gensim.utils.simple_preprocess(line)
#             try:
#                 x = gensim.utils.simple_preprocess(rewritten_intent)
#                 # TODO: check if it splits package.class.function correctly at the dots.
#                 # all_english_lines.append(x)
#                 # NOT TESTED YET:
#                 lowers = text.lower()
#                 no_punctuation = lowers.translate(None, string.punctuation)
#                 # dict_of_questions_and_code[file] = no_punctuation
#                 stemmed_and_tokenized = tokenize(no_punctuation)
#                 all_english_lines.append(stemmed_and_tokenized)
#
#             except:
#                 continue
#             #print()
#
#             # # from gensim.models import FastText
#             # # # [...]
#             # # sentences = SentencesIterator(tokens_generator)
#             # # model = FastText(sentences)
#     return all_english_lines



print()
# ----------------------------------------------------- do tokenizing (& stemming optionally too) ---------------------------------------------------------
print()

dict_of_SOquestions_stemmed___to___original_SOquestions = return_data_as_dict_of_SOquestions_stemmed____to____original_sentences_____for_word2vec_input_format(dict_of_questions_and_code_TRAIN)
# try:
#     code_for_empty_entry = list_of_SOquestions___stemmed_and_tokenized[]
# except:
#     print("GOOD -- no empty entry in SOquestions")

# for key, value in dict_of_SOquestions_stemmed___to___original_SOquestions.items():
#     print(key+" --> "+value)
#sys.exit() # multidimensional still present here, in both key and value ...

print()
# ----------------------------------------------------- /do tokenizing (& stemming optionally too) ---------------------------------------------------------
print()


print()
# ----------------------------------------------------- train word2vec on tokenized data: ---------------------------------------------------------
print()

if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
    list_of_SOquestions_stemmed = [stemmed_SOquestion.split(" ") for stemmed_SOquestion in dict_of_SOquestions_stemmed___to___original_SOquestions.keys()]
else:
    list_of_SOquestions_stemmed = [tokenize(stemmed_SOquestion) for stemmed_SOquestion in dict_of_SOquestions_stemmed___to___original_SOquestions.keys()]

# build vocabulary and train model
model = gensim.models.Word2Vec(
    list_of_SOquestions_stemmed, # to test OLD WAY: change this param to dict_of_SOquestions_stemmed___to___original_SOquestions
    size=200, #150, #500, # 150, 1000, no effect really, 50 brings 1 bleu point down
    #size=500,
    #size=1000, # CHANGE --> at 500 BLEU 14.44, at 1000 BLEU is 14.53
    #size=100, # at 50 BLEU 14.75, at 150 BLEU is 15.28 .... ok actually that's just a fluke, they're all around 14.5, the epochs param is what matters
    #window=10,
    window=5, # 5, 10, 100 (brought slightly down but probably just chance), 1 slightly down too, best is 5
    min_count=1, # 0
    workers=10)
model.train(
    list_of_SOquestions_stemmed,
    total_examples=len(list_of_SOquestions_stemmed),
    #epochs=10,
    epochs=100, # CHANGE!!! epochs=100 increased score by a lot: 15 BLEU, while 1000 brought it down at 13.91 ... 500 seems to not affect results negatively yet.
    #epochs=1000 # strangely brought the score down by a bit: 14 BLEU, I guess there's overfitting after a point.
)
# OLD WAY: model.train(dict_of_SOquestions_stemmed___to___original_SOquestions, total_examples=len(dict_of_SOquestions_stemmed___to___original_SOquestions), epochs=10)

model.save("word2vec.model")
# model = Word2Vec.load("word2vec_BIG.model")
model = Word2Vec.load("word2vec.model")

try: # NB: calling it once seems necessary in order to trigger getting the normalized w2vec vectors. otherwise normalized version is not available at retrieve time.
    w1 = "["
    print(w1)
    most_similar = model.wv.most_similar(positive=w1)
    print(most_similar)
except Exception as e:
    print(e)

#custompk._meta.pk.name
try: # NB: calling it once seems necessary in order to trigger getting the normalized w2vec vectors. otherwise normalized version is not available at retrieve time.
    w1 = "custompk._meta.pk.name"
    print(w1)
    most_similar = model.wv.most_similar(positive=w1)
    print(most_similar)
except Exception as e:
    print(e)
# sys.exit()
#
# try:
#     w1 = "."
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = ")"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "sum"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "open"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "x"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "*"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# w2vec_vector_TEST = model.wv.word_vec("x", use_norm=True)
# print(w2vec_vector_TEST)
# sys.exit()




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
#
#
# try:
#     w1 = "dictionary"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "array"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
#
# try:
#     w1 = "sort"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
#
# try:
#     w1 = "pip"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "loop"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "integer"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "dirty"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "multidimensional"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "integ"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "multidimension"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# try:
#     w1 = "longest"
#     print(w1)
#     most_similar = model.wv.most_similar(positive=w1)
#     print(most_similar)
# except Exception as e:
#     print(e)
#
# # sys.exit() # multidimension present in word2model at param size=1000
# # print()


# #
# try:
#     path = get_tmpfile("wordvectors.kv")
#     model.wv.save(path)
#     wv = KeyedVectors.load("model.wv", mmap='r')
#     vector = wv['computer']  # numpy vector of a word
# except Exception as e:
#     print(e)


# # https://radimrehurek.com/gensim/similarities/index.html
# from gensim.similarities.index import AnnoyIndexer
# indexer = AnnoyIndexer(model, 2)
# model.most_similar("cat", topn=2, indexer=indexer)

# # get the distance between two sentences:
# sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
# sentence_president = 'The president greets the press in Chicago'.lower().split()
# similarity = model.wv.wmdistance(sentence_obama, sentence_president)
# print("{:.4f}".format(similarity))

# get distance between two words:
# >>> distance = word_vectors.distance("media", "media")
# >>> print("{:.1f}".format(distance))
# 0.0

# get distance between arrays of words:
# >>> sim = word_vectors.n_similarity(['sushi shop'], ['japanese restaurant'])
# >>> print("{:.4f}".format(sim))
# 0.7067

# # here's how to do it:
# your_word_vector = [0,0,0,0,0,0]
# model.most_similar(positive=[your_word_vector], topn=1))
#
# #
# model.wv.similar_by_vector(vector, topn=10, restrict_vocab=None)

print()
# ----------------------------------------------------- /train word2vec on tokenized data: ---------------------------------------------------------
print()




print()
# ----------------------------------------------------- train TF-IDF on tokenized data too: ---------------------------------------------------------
print()


# https://github.com/RaRe-Technologies/gensim/blob/1f357a7c4db27ea9c946dbc6942d82b00815a55e/gensim/models/keyedvectors.py#L510
# compute the weighted average of all words
from numpy import ndarray
from numpy import array
from numpy import float32 as REAL


# # --DONE TODO: tf idf not done yet:
# # https://radimrehurek.com/gensim/tutorial.html
# import gensim.downloader as api
# from gensim.models import TfidfModel
# from gensim.corpora import Dictionary
# # dataset = api.load("text8")
# dataset = documents
# dct = Dictionary(dataset)  # fit dictionary
# corpus = [dct.doc2bow(line) for line in dataset]  # convert corpus to BoW format
# model = TfidfModel(corpus)  # fit model
# # index_of_word = dct.["datetime"]
# vector = model[corpus[0]]  # apply model to the first corpus document


# import nltk
# import string
# import os
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.stem.porter import PorterStemmer

# path = '/opt/datacourse/data/parts'
# dict_of_questions_and_code = {}
# stemmer = PorterStemmer()
#
# # def stem_tokens(tokens, stemmer):
# #     stemmed = []
# #     for item in tokens:
# #         stemmed.append(stemmer.stem(item))
# #     return stemmed
# #
# # def tokenize(text):
# #     tokens = nltk.word_tokenize(text)
# #     stems = stem_tokens(tokens, stemmer)
# #     return stems
#
# for subdir, dirs, files in os.walk(path):
#     for file in files:
#         file_path = subdir + os.path.sep + file
#         shakes = open(file_path, 'r')
#         text = shakes.read()
#         lowers = text.lower()
#         no_punctuation = lowers.translate(None, string.punctuation)
#         dict_of_questions_and_code[file] = no_punctuation

#this can take some time # https://stackoverflow.com/questions/20132070/using-sklearns-tfidfvectorizer-transform

def my_preprocessor(my_param):
    my_a_8745tbhjkfgk = 5
    print("INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE")
    print(my_param)
    if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
        return my_param.lower() #my_param.lower() #my_param.split(" ")
    else:
        return my_param.lower() #my_param.split(" ")
def my_tokenizer(my_param):
    print("INSIDE_CALLABLE_2_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE_INSIDE_CALLABLE")
    print(my_param)
    if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
        #return my_param #my_param.split(" ")
        #return tokenize(my_param)
        return my_param.split(" ")
    else:
        return my_param.split(" ")

if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
    max_df_value = 1.0
else:
    max_df_value = 0.71
tfidf = TfidfVectorizer(
    #tokenizer=tokenize, # can lead to twice-tokenization? eg multidimensional-->multidimension-->multidimen?
    #stop_words='english',
    stop_words=None,
    min_df=0, #0.000000000000001,
    max_df=max_df_value, #0.71,#helps at .71
    # ngram_range=(1,5), # TO TRY !!!!!! didn't change anything ... 3-gram: BLEU=15.84, 5-gram: BLEU=15.37,16.16,15.23,
    max_features=None,
    binary=True,
    sublinear_tf=True,
    preprocessor=my_preprocessor, #lambda x: a=0,
    tokenizer=my_tokenizer,
) # If None, no stop words will be used. max_df can be set to a value in the range [0.7, 1.0) to automatically detect and filter stop words based on intra corpus document frequency of terms.
# --DONE, TODO: more params to try: tfidf = TfidfVectorizer( --DONE
# max_features=10,
# strip_accents='unicode',
# analyzer='word',
# stop_words=stop_words.extra_stopwords,
# lowercase=True,
# use_idf=True)

# tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', stop_words='english', vocabulary=vocabulary)
# tfs = tfidf.fit_transform(dict_of_questions_and_code_TRAIN.keys()) # --DONE TODO: source of the bug, test now. FUCK. ALRIGHT. FINALLY.
#  --DONE TODO: check if improved?????????????? YEAH 16.23, 15.53, 15.56, 15.69, 15.11,  .... when no 0.0: 15.12, 15.37, 15.12, 15.66
tfs = tfidf.fit_transform(dict_of_SOquestions_stemmed___to___original_SOquestions.keys())

# ----- a test: -----
try:
    multidimension_string_word = tfidf.vocabulary_["multidimension"]
    print("multidimension_string_word")
    print(multidimension_string_word)
except Exception as e_23465798:
    print(e_23465798)
# sys.exit()
# ----- /a test: -----


# ---- SOME TEST: ------
# flag_multidimensional = False
# for key in dict_of_questions_and_code_TRAIN.keys():
#     if "multidimensional" in key:
#         #print("FOUND")
#         flag_multidimensional = True
#     # elif "multidimension" in key:
#     #     #print("FOUND")
#     #     flag_multidimensional = True
#     # #else:
#     #     #print("ERROR, ABORTING, MULTIDIMENSION/AL not found!!!!!!!!!!!!!!!!!!!!!!!!")
# if flag_multidimensional == True:
#     print("FOUND")
# else:
#     print("ERROR, ABORTING, MULTIDIMENSION/AL not found!!!!!!!!!!!!!!!!!!!!!!!!")
# sys.exit()
# ---- /SOME TEST: ------

print("vectorizer.get_feature_names() --> "+str(tfidf.get_feature_names()))

# tfidf_features_1 = tfidf.get_feature_names()
# for x in tfidf_features_1:
#     print(x)
# #sys.exit()

# # --DONE no that's fine, no need for this code just below ... so what fixed it? TODO check if this is what fixed multidimension being omitted ...
# tfidf_matrix_dense_1 = tfs.todense()
# # print(tfidf_matrix_dense_1)
# for x in tfidf_matrix_dense_1:
#     print(x)
# # sys.exit()
# tfidf_features_1 = tfidf.get_feature_names()

# import pandas as pd
# df = pd.DataFrame(tfidf_matrix_dense_1, columns = tfidf_features_1, index=["Tf-Idf"])
# print("-----------")
# print(df.to_string())


tfidf_vocab_by_id = {} # so we can retrieve words from their ids later ...
for word, id in tfidf.vocabulary_.items():
    tfidf_vocab_by_id[id] = word
    #print("\n")
    print(str(id)+" --> "+str(word))

# # ---- test, passed, ok -----
# if "multidimension" not in tfidf.vocabulary_.keys():
#     print("'multidimension' not in tfidf.vocabulary.values()")
# sys.exit() # still contains multidimension ... continuing downwards
# # ---- /test -----

# # trying again:
# from sklearn.feature_extraction.text import CountVectorizer
# count_vect = CountVectorizer()
# count_vect = count_vect.fit(train_data)
# freq_term_matrix = count_vect.transform(train_data)
# from sklearn.feature_extraction.text import TfidfTransformer
# tfidf = TfidfTransformer(norm=”l2")
# tfidf.fit(freq_term_matrix)
# doc_freq_term = count_vect.transform([doc])
# doc_tfidf_matrix = tfidf.transform(doc_freq_term)



# # str = 'this sentence has unseen text such as computer but also king lord juliet'
# response = tfidf.transform([s])
# print(response)

print()
# ----------------------------------------------------- /train TF-IDF on tokenized data too: ---------------------------------------------------------
print()





print()
# ----------------------------------------------------- build KNN vector space: ---------------------------------------------------------
print()

def get_tfidf_weights_for_words_in_sentence(sentence):
    print("new sentence -----------> "+sentence)

    # str = 'this sentence has unseen text such as computer but also king lord juliet'

    # # CHANGE_BUG_OLD:
    # response = tfidf.transform([' '.join(sentence)])
    # # /CHANGE_BUG_OLD:

    # CHANGE_BUG_NEW:
    global tfidf

    # test:
    for x_my in sentence.split(" "):
        print(x_my)
        if x_my not in tfidf.vocabulary_.keys():
            print(str(x_my)+" not in tf-idf vocab")
            #sys.exit()
    # /test

    response = tfidf.transform([sentence]) # https://stackoverflow.com/questions/20132070/using-sklearns-tfidfvectorizer-transform
    print(response)
    current_multidimension_index = -1

    # test:
    for x_my in sentence.split(" "):
        print(x_my)
        if x_my not in tfidf.vocabulary_.keys():
            print(str(x_my)+" not in tf-idf vocab")
            #sys.exit()
    # /test

    try:
        print("&&&&&&")
        current_multidimension_index = tfidf.vocabulary_["multidimension"]
        print("success finding multidimension in tf-idf vocab")
    except:
        pass
    try:
        retrieved_word_woah = tfidf_vocab_by_id[current_multidimension_index]
        print(retrieved_word_woah)
        print("success finding multidimension's in tf-idf vocab id index")
        # retrieved_word_woah = tfidf_vocab_by_id[1236]
        # print(retrieved_word_woah)
    except:
        pass
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(tfidf.idf_)
    print(len(tfidf.idf_))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #sys.exit()
    response_as_array = response.todense() #toarray()
    for x in response_as_array:
        for y in x:
            print("new entry in response_as_array")
            print(y)
    #sys.exit()

    #print("response = tfidf.transform([sentence]) --> " + str(response.indices))

    # tfidf_matrix_dense = response.todense()
    # #print(tfidf_matrix_dense)
    # for x in tfidf_matrix_dense:
    #     for y in x:
    #         for z in y:
    #             print(str(z))
    # #sys.exit()

    # tfidf_features = tfidf.get_feature_names()
    # for x in tfidf_features:
    #     print(str(x))
    # print(str(tfidf_features))
    # # sys.exit()

    # import pandas as pd
    # df = pd.DataFrame(tfidf_matrix_dense, columns = tfidf_features, index=["Tf-Idf"])
    # print("-----------")
    # print(df.to_string())
    # #sys.exit()

    # for x in response.indices:
    #     retrieved_word = tfidf_vocab_by_id[x]
    #     print(retrieved_word)
    # #sys.exit()

    print("------")
    # /CHANGE_BUG_NEW

    # -----CHANGE_OLD_12345-----
    # print(response)
    # integer_id = tfidf.vocabulary_["concaten"] # concaten is 1061
    # print(integer_id)
    positive_func = []
    tf_idf_word_index = -1
    retreived_word = ""
    for word_counter in range(0, len(response.data)): #len(response_as_array)):
        retreived_word = ""
        tf_idf_word_index = ""
        tf_idf_word_index = response.indices[word_counter]
        retreived_word = tfidf_vocab_by_id[tf_idf_word_index]
        print(str(tf_idf_word_index) +" --> "+ str(retreived_word))
        positive_func.append((retreived_word, response.data[word_counter]))
    # OLD WAY without tf-idf: positive_func = [(word, 1.0) for word in sentence]
    # adjust, using tf idf weights:
    # vector_of_weighted_words_given_sentence_in_correct_weird_format = model[corpus[0]]
    if not positive_func or positive_func is None:
        print("positive_func is empty for sentence --> " + str(sentence)) # --NEVER HAPPENS ANYMORE TODO: I think this happens and it's ok, but look into it later ...
        sys.exit()
    print(" ----- bis? ------")
    for x in positive_func:
        print(x)
    # sys.exit()

    # # ugly fix:
    # positive_func_KEYS = [i[0] for i in positive_func]
    # for x in sentence.split(" "):
    #     if x not in positive_func_KEYS:
    #         print("word not in tf-idf weights returned, had to add it with an arbitrary tf-idf weight --> " + x)
    #         # -----CHANGE_bobobobobo_OLD----- BLEU: 15.72, 16.00, 15.72, 15.81, 15.47, 15.69,
    #         positive_func.append((x, 0.0)) # --DONE --TODO: test whether this fix has any impact. NO CHANGE: BLEU=15.79 ... 15.62
    #         #sys.exit() # now that multidimensional never bugs anymore, signal is accepted: words never seen at training
    #         # -----CHANGE_bobobobobo_OLD-----
    #
    #         # # -----CHANGE_bobobobobo_NEW----- BLEU --> 15.77, 15.32, 15.60, 15.77, 15.94
    #         # multidimension_word_index = tfidf.vocabulary_[word]
    #         # weight_from_todense = response_as_array[0, multidimension_word_index]
    #         # positive_func.append((x, weight_from_todense)) # --DONE TODO: any impact? ... no significant impact
    #         # # -----CHANGE_bobobobobo_NEW-----

    # -----/CHANGE_OLD_12345-----

    # # ------CHANGE_NEW_12345-------- makes BLEU slightly worse by one point ... 14.47, 14.77, 14.59, 14.74, WHEREAS THE OLD WAY GAVE: 16.12, 15.77, -------
    ##### but accoridng to SO question, it's really the correct way .... https://stackoverflow.com/questions/25902119/scikit-learn-tfidfvectorizer-meaning
    ##### thing is, multidimension is still absent from the tf-idf vocab ... so reall what's the point, screwing things up for not even fixing the quirk ...
    # ####multidimension_string_word = tfidf.vocabulary_["multidimension"]
    # positive_func = []
    # sentence_split = sentence.split(" ")
    # # if len(sentence_split) != len(response_as_array):
    # #     print("ERROR, ABORTING --> len(sentence.split(" ")) != len(response_as_array) ")
    # #     print(sentence.split(" "))
    # #     print(response_as_array[0])
    # #     print(len(sentence.split(" ")))
    # #     print(len(response_as_array[0]))
    # #     sys.exit()
    #
    # for i in range(len(sentence_split)):
    #     word = sentence_split[i]
    #
    #     if not word in tfidf.vocabulary_.keys():
    #         print("WORD NOT IN VOCAB, INSPECT IF NORMAL")
    #         print("word --> " +str(word))
    #         print("sentence --> " + str(sentence))
    #         #sys.exit()
    #         word_weight = 0.0
    #     else:
    #         multidimension_word_index = tfidf.vocabulary_[word]
    #         print("len(response_as_array)")
    #         print(len(response_as_array))
    #         #word_weight = response_as_array[0][multidimension_word_index] # WHEN USING response.toarray() // this is actually not the weight, it's something else ... or an old weight?
    #         word_weight = response_as_array[0, multidimension_word_index] # WHEN USING response.todense() // this is actually not the weight, it's something else ... or an old weight?
    #
    #         #word_in_vocab = tfidf.vocabulary_[word]
    #         print("word_in_vocab? --> " +str(multidimension_word_index))
    #
    #     positive_func.append((word, word_weight))
    #     #positive_func.append((word, response.data[i]))
    #
    # # ------/CHANGE_NEW_12345--------

    # if "multidimensional" in sentence.split(" "):
    #     sys.exit()
    # if "multidimension" in sentence.split(" "):
    #     sys.exit()

    return positive_func # --FINE, it's just variable names or hex, etc. // TODO: found a bug here ... why are these all letters instead of words ??????

def get_mean_for_sentence(positive):
    """
    @param: sentence, as 2D array of "words with their corresponding weight": e.g. [(word, 1.0) for word in sentence_to_be_avgd]
    :return: the weighted average of all words in sentence:
    """
    all_words, mean = set(), []
    for word, weight in positive:# + negative:
        print("----------- processing new word in sentence for getting mean of sentence -----------")
        if isinstance(word, ndarray):
            mean.append(weight * word)
            sys.exit() # should never get here.
        else:
            try:
                # ---- /test-----
                my_variable = "x"
                print(my_variable)
                print(word)
                print(weight)
                # ---- /test-----

                w2vec_vector = model.wv.word_vec(word, use_norm=True) # ... why can't I use the normalized vectors on code-token vector space????
                #w2vec_vector = model.wv.word_vec(word, use_norm=False) # ... why can't I use the normalized vectors on code-token vector space????
                # print(w2vec_vector)
                # if word isn't in the vocab, w2vec_vector is not returned, and an exception is thrown --> we catch it and simply discard the word for the avg ... compute the avg without it.
                import numpy as np
                x = np.array(w2vec_vector)
                np.linalg.norm(x)
                w2vec_vector_NORMALIZED = x
                # print(w2vec_vector_NORMALIZED)

                # # ---- sanity check -----
                # for i in range(0, len(w2vec_vector)):
                #     value_before_normalization = w2vec_vector[i]
                #     value_AFTER_normalization = w2vec_vector_NORMALIZED[i]
                #     ratio = value_before_normalization / value_AFTER_normalization
                #     print(ratio) # it's always one, I'm assuming because the w2vec code does normalization within it.
                # # ----- /sanity check: ----

                new_w2vec_vector_weighted_with_tfidf = weight * w2vec_vector_NORMALIZED
                # print(new_w2vec_vector_weighted_with_tfidf)

                # # ---- sanity check -----
                # for i in range(0, len(new_w2vec_vector_weighted_with_tfidf)):
                #     value_before_tfidf = w2vec_vector_NORMALIZED[i]
                #     value_AFTER_tfidf = new_w2vec_vector_weighted_with_tfidf[i]
                #     ratio =  value_AFTER_tfidf / value_before_tfidf
                #     print(ratio)
                # print("this was the weight --> "+ str(weight))
                # # sys.exit()
                # # ----- /sanity check: ----



                # --GOOD TODO: NB: here w2vec_vector will be None for new words, and also for n-grams ... I could train on n-grams if I wanted, but if they're only in tf-idf it won't serve any purpose.

                # new_w2vec_vector_weighted_with_tfidf_NEW = []
                # for component in w2vec_vector:
                #     new_component = weight * component
                #     new_w2vec_vector_weighted_with_tfidf_NEW.append(new_component)
                # for i in range(0, len(new_w2vec_vector_weighted_with_tfidf_NEW)):
                #     if new_w2vec_vector_weighted_with_tfidf_NEW[i] != new_w2vec_vector_weighted_with_tfidf[i]:
                #         print("ERROR, ABORTING --> new_w2vec_vector_weighted_with_tfidf_NEW[i] != new_w2vec_vector_weighted_with_tfidf[i] ... ")
                #         print(new_w2vec_vector_weighted_with_tfidf_NEW[i])
                #         print(new_w2vec_vector_weighted_with_tfidf[i])
                #         sys.exit()

                # # ----------test: PASSED, NICE------------
                # if len(w2vec_vector) != len(new_w2vec_vector_weighted_with_tfidf):
                #     print("wtf")
                #     sys.exit()
                # for i in range(0, len(w2vec_vector)):
                #     print("~~~~~~")
                #     print(w2vec_vector[i])
                #     print(new_w2vec_vector_weighted_with_tfidf[i])
                #     print(w2vec_vector[i] / new_w2vec_vector_weighted_with_tfidf[i])
                #
                # # import sympy
                # # import numpy as np
                # # mat = np.array([w2vec_vector, new_w2vec_vector_weighted_with_tfidf])  # your matrix
                # # _, inds = sympy.Matrix(mat).T.rref()   # to check the rows you need to transpose!
                # # print(inds)
                # # if len(inds) > 0:
                # #     print("ERROR, ABORTING --> multiplying w2vec vectors by tf-df weights results in weird transformation ... ")
                # #     sys.exit()
                # # ----------/test: PASSED, NICE------------

                # type(new_w2vec_vector_weighted_with_tfidf)
                # type(new_w2vec_vector_weighted_with_tfidf.tolist())
                mean.append(new_w2vec_vector_weighted_with_tfidf)
                # print("mean: ")
                # print(mean)

                # ---- test code: ----
                if word in model.wv.vocab:
                    all_words.add(model.wv.vocab[word].index)
                else:
                    print("word not in w2vec vocab? word = "+str(word)+" ... --> "+str(e))
                    sys.exit() # --FINE, --TODO: this case is impossible anyway since if the word isn't in the vocab, w2vec model throws an exception when retrieving its w2vec vector (and that exception is caught below).
                # ---- /test code: ----

            except Exception as e_1:
                print(e_1)
                print("word not in w2vec vocab? word = "+str(word))
                print(" --> "+str(e_1))
                # sys.exit() # --FINE, --TODO: this should not happen, debug this.
                # no actually is happens all the time that
                # - query words arent seen at training ...
                # - n-grams (if I turn them on in the tf-idf params), since they aren't used for training w2vec ... so aren't found in the w2vec model.
                pass
    if not mean:
        #raise ValueError("cannot compute similarity with no input")
        print("cannot compute similarity with no input")
        #mean.append([0.0])
        #mean = numpy.array([0,0,0])
        mean.append(0.0 * model.wv.word_vec("none", use_norm=True))   # --NEVER HAPPENS ANYMORE, put a sys.exit() if happens TODO: improve on this dirty fix ... but anyway it never happens, shold never happen
        sys.exit() # actually we should ignore new words, not set them to zero, which would skew the avg ... so abort in this case.
    sentence_vector_mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)
    # print("mean --> "+str(mean))  # this is great
    # print("mean --> "+str(sentence_vector_mean))  # ?

    # --DONE, DUN AND DUN (actually it was already done by w2vec implement.) TODO: normalize the result, too, as in the formula in the paper!
    import numpy as np
    x = np.array(sentence_vector_mean)
    np.linalg.norm(x)
    sentence_vector_mean_NORMALIZED = x
    # print(sentence_vector_mean_NORMALIZED)

    # # ---- sanity check -----
    # for i in range(0, len(sentence_vector_mean_NORMALIZED)):
    #     value_before_normalization = sentence_vector_mean[i]
    #     value_AFTER_normalization = sentence_vector_mean_NORMALIZED[i]
    #     ratio = value_before_normalization / value_AFTER_normalization
    #     print(ratio)
    # # sys.exit()
    # # ----- /sanity check: ----

    return sentence_vector_mean_NORMALIZED

# # but this is not what I want ... I want sentences:
# most_sim_final = model.wv.similar_by_vector(sentence_vector_mean, topn=10, restrict_vocab=None)
# print("most_sim_final --> "+str(most_sim_final))

# most_sim_final --> [('to', 0.6668168902397156), ('can', 0.6008535623550415), ('in', 0.580234944820404), ('python', 0.5465377569198608), ('of', 0.5437493324279785), ('with', 0.523889422416687), ('and', 0.5155302882194519), ('do', 0.5143002271652222), ('the', 0.4938086271286011), ('for', 0.44129064679145813)]
# Process finished with exit code 0


# actually I need to:
# 1- DONE: avg words in query sentence
# 2- avg words in all SO posts
# 3- use scikit library on that dataset to find the KNNs
# // 3- use Annoy library on that dataset to find the KNNs


import hashlib
def hashFor(data):
    # Prepare the project id hash
    hashId = hashlib.md5()
    hashId.update(repr(data).encode('utf-8'))
    return hashId.hexdigest()


# ------- Actually build the KNN vector space with this loop:
# build dataset of sentences for KNN:
# this btw could be done only once for any dataset, it's a bit long:
dataset_of_sentence_vectors_for_KNN = []
hash_of_coordinates_to_original_sentence = {}
i=0
for doc_stemmed, doc in dict_of_SOquestions_stemmed___to___original_SOquestions.items():  # , doc
    if not doc_stemmed or doc_stemmed == []:
        print("document has empty question after stemming ... "+str(doc_stemmed))
        sys.exit()
    i += 1
    positive_doc = get_tfidf_weights_for_words_in_sentence(doc_stemmed)  # [(word, 1.0) for word in sentence_to_be_avgd]
    if positive_doc is None or 'none' in positive_doc:
        print("if positive_doc is None or 'none' in positive_doc:")
        sys.exit()
    for x in positive_doc:
        print(x)
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

# --WTVER, SINCE RERUNNING EVERyTIME NOW (I can wait, data is small) TODO: fix lossy serialization of dataset:
# # --WTVZ TODO: save these as files, a serialized list and a serialized hash ... and load them instead
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
# # --WTVZ TODO: save these as files, a serialized list and a serialized hash ... and load them instead
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




print()
# ----------------------------------------------------- /build KNN vector space: ---------------------------------------------------------
print()







print()
# ----------------------------------------------------- traverse test set and build list of code answers: ---------------------------------------------------------
print()

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



# add Jun 2019: to get BLEU4 score the conala.sh way:
list_of_results_to_write_to_json_file_for_BLEU4_eval = []
list_of_QUERIES_to_write_to_json_file_for_BLEU4_eval = []
def getBleuScoreForSearchQuery_AndAddResultToListOfResults(english_query, reference_answer_as_code):

    #sentence_to_be_avgd = gensim.utils.simple_preprocess(s)
    # sentence_to_be_avgd = s.split(" ")

    # --DONE TODO: here make sure to use the exact same tokenization-stemming function as used for training ... otherwise matches wont work ...
    # sentence_to_be_avgd = tokenize(s)   # old code for parsing one query at a time
    sentence_to_be_avgd = tokenize(english_query) # dont tokenize twice, leads to multidimensional-->multidimension-->multidimens
    #sentence_to_be_avgd = english_query.split(" ")
    #sentence_to_be_avgd = nltk.word_tokenize(english_query)
    # --DONE /TODO: here make sure to use the exact same tokenization-stemming function as used for training ... otherwise matches wont work ...

    for word in sentence_to_be_avgd:
        print(word)
        # multidimension still present!!!

    if not sentence_to_be_avgd or len(sentence_to_be_avgd) == 0 or sentence_to_be_avgd == [] or None in sentence_to_be_avgd:
        print("sentence_to_be_avgd is empty after stemming and tokenization ... for sentence-query --> " + str(english_query))
        sys.exit()
    # dict_of___English___to___stemmed_and_tokenized_English.append(stemmed_and_tokenized)
    sentence_to_be_avgd = " ".join(sentence_to_be_avgd)

    positive_query = get_tfidf_weights_for_words_in_sentence(sentence_to_be_avgd)  # [(word, 1.0) for word in sentence_to_be_avgd]
    print("---is multidimension still rpesent now?-----") # no it's not
    if positive_query is None or 'none' in positive_query:
        print("if positive_query is None or 'none' in positive_query:")
        print(positive_query)
        sys.exit()
    for x in positive_query:
        print(x)
    #sys.exit()
    # --FIXED, just needed to train tf-idf on stemmed corpus TODO: fix bug: gensim.utils.simple_preprocess(s) removes the word multidimensional from the sentence ... why?
    sentence_vector_mean_QUERY = get_mean_for_sentence(positive_query)


    # For the simple task of finding the nearest neighbors between two sets of data,
    # the unsupervised algorithms within sklearn.neighbors can be used:
    # ... Because the query set matches the training set,
    # the nearest neighbor of each point is the point itself, at a distance of zero.
    from sklearn.neighbors import NearestNeighbors
    import numpy as np
    # X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])   # dummy dataset of vectors
    X = np.array(dataset_of_sentence_vectors_for_KNN)   # real dataset of vectors
    #nbrs = NearestNeighbors(n_neighbors=5, leaf_size=1, algorithm='brute').fit(X)
    num_neighbours_you_want = NUM_NEIGHBOURS_TO_OUTPUT #20
    nbrs = NearestNeighbors(
        n_neighbors=num_neighbours_you_want,
        #weights='distance', # TODO: any impact? ... param isn't recognized, maybe only in earlier versions of this library
        leaf_size=1, # 1 is to try to get the best answer ... not seeing any impact though.
        algorithm='brute',
        #p=2,
        p=1, #Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.
    ).fit(X)
    # TODO: why is brute not working? it always gives slightly different answers at every run
        # ‘ball_tree’ will use BallTree
        # ‘kd_tree’ will use KDTree
        # ‘brute’ will use a brute-force search.
        # ‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.
    # distances, indices = nbrs.kneighbors(X)   # on itself ...
    # distances, indices = nbrs.kneighbors([[-1, -0.9]])  # dummy data point
    distances, indices = nbrs.kneighbors([sentence_vector_mean_QUERY], num_neighbours_you_want)  # real search query vector data point
    print("distances and indices:")
    print(distances)
    print(indices)

    for indices_unwrapped in indices:
        is_first_ie_best_result = True
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

                # # --- just testing code, no need to get the weighted vector for the sentence match ----
                # positive_match = get_tfidf_weights_for_words_in_sentence(best_sentence_match_to_query)  # [(word, 1.0) for word in sentence_to_be_avgd]
                # if positive_doc is None or 'none' in positive_doc: # and wtf is positive_doc doing here?
                #     print("if positive_doc is None or 'none' in positive_doc:")
                #     sys.exit()
                # print(" ----- bis? ------")
                # for x in positive_match:
                #     print(x)
                # # --- just testing code, no need to get the weighted vector for the sentence match ----

                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code: ")
                corresponding_original_SOquestion = dict_of_SOquestions_stemmed___to___original_SOquestions[best_sentence_match_to_query]
                corresponding_code = dict_of_questions_and_code_TRAIN[corresponding_original_SOquestion]
                print(corresponding_code)

                #import conala_eval why not found....
                # FIXED --> the slight changes in bleu scores are just due to tree impl. of KNN --> CHANGE: replace reference_answer_as_code with code, as it was before ... why is it giving a slightly different BLEU score?
                get_BLEU_score_for_2_strings___CONALA_way(reference_answer_as_code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
                get_BLEU_score_for_2_strings___CONALA_way(english_query, corresponding_original_SOquestion, is_BLEU_for_code_evaluation_NOT_matchedQuery=False)
                print("bleu nltk for comparisno: ")
                get_BLEU_score_for_2_strings___NLTK_way(reference_answer_as_code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
                get_BLEU_score_for_2_strings___NLTK_way(english_query, corresponding_original_SOquestion, is_BLEU_for_code_evaluation_NOT_matchedQuery=False)

                # --------- Add, Jun 2019: ----------
                # to get BLEU4 the same way the conala.sh gets it: write all results to file in same format as annot.test.json:
                if is_first_ie_best_result: #num_neighbours_you_want == 1:
                    list_of_results_to_write_to_json_file_for_BLEU4_eval.append(corresponding_code)
                    list_of_QUERIES_to_write_to_json_file_for_BLEU4_eval.append(english_query)
                    is_first_ie_best_result = False
                # else:
                #     print("WARNING, CANT PRODUCE JSON FILE FOR CONALA EVALUATION: num_neighbours_you_want VARIABLE IS NOT SET TO 1 --> SET IT TO 1")

                if code != reference_answer_as_code:
                    print(" ERROR, ABORTING --> code != reference_answer_as_code")
                    print("code --> "+code)
                    print("reference_answer_as_code --> "+reference_answer_as_code)
                    sys.exit()
                # --------- /Add, Jun 2019: ----------

            except Exception as e:
                print("error retrieving original document")
                print(e)
                sys.exit()
                pass

    # use this to verify if it's finally fixed ... doesn't change much when I make it zero manually: BLEU=15.95 ... 15.91 ...
    # if "multidimensional" in english_query:
    #     sys.exit()

 # ---- Actually call the functions: get code answer predicted .... for each test set question:
# load the reference translations:
input_file_REFERENCE = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-test.json"
dict_of_questions_and_code_REFERENCE = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file_REFERENCE, is_jsonl_binary_file=False, isForReferenceFile=True)


# old way, now reverse it right away as we build it:
# if IS_IN_REVERSE___IE_CODE_2_ENGLISH:
#     len_before = len(dict_of_questions_and_code_REFERENCE)
#     dict_of_questions_and_code_REFERENCE = {v: k for k, v in dict_of_questions_and_code_REFERENCE.items()}
#     len_after = len(dict_of_questions_and_code_REFERENCE)
#     if len_before != len_after:
#         print("before, after")
#         print(len_before)
#         print(len_after)
#         print("aborting, length of dict got different after it was reversed ... collisions of keys?")
#         sys.exit()


if len(dict_of_questions_and_code_REFERENCE) != 500:
    print("ERROR, ABORTING --> reading conala-test.json test set file yields less than 500 entries .... ")
    print("len(dict_of_questions_and_code_REFERENCE) --> "+ str(len(dict_of_questions_and_code_REFERENCE)))
    sys.exit()
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

    getBleuScoreForSearchQuery_AndAddResultToListOfResults(SOquestion, code)

    print()


print()
# ----------------------------------------------------- /traverse test set and build list of code answers: ---------------------------------------------------------
print()





print()
# ----------------------------------------------------- write answers to json for later eval with sudo bash conala_baseline_EVAL_ONLY_FOR_FACEBOOK.sh: ---------------------------------------------------------
print()

# ADD NIC jun 2019:
# get overall BLEU4 score using the same line as the bash script -->
# 1) first, produce the files in the same format ...
# 2) call the same line --> but actually just do it later by running a bash script that contains only that line:
    # # Calculate the BLEU score
    # python $SDIR/eval/conala_eval.py --strip_ref_metadata --input_ref conala-corpus/conala-test.json --input_hyp results/$setting.test.json
import json
with open('FACEBOOK_CODE_2_ENG.test.json', 'w') as outfile_results_conala_eval:
    json.dump(list_of_results_to_write_to_json_file_for_BLEU4_eval, outfile_results_conala_eval)
with open('FACEBOOK_CODE_2_ENG.queries.json', 'w') as outfile_QUERIES_conala_eval:
    json.dump(list_of_QUERIES_to_write_to_json_file_for_BLEU4_eval, outfile_QUERIES_conala_eval)

# # ---- adding test's (answer's) English -----
# with open('FACEBOOK_CODE_2_ENG.test_ENG.json', 'w') as outfile_results_conala_eval:
#     json.dump(list_of_results_to_write_to_json_file_for_BLEU4_eval, outfile_results_conala_eval)
# # ---- adding queries' (questions') code -----
# with open('FACEBOOK_CODE_2_ENG.queries_CODE.json', 'w') as outfile_QUERIES_conala_eval:
#     json.dump(list_of_QUERIES_to_write_to_json_file_for_BLEU4_eval, outfile_QUERIES_conala_eval)



# query: s = "print variable value without spaces"   # really good matches
# best_sentence_match_to_query:
# ['print variable value without spaces']
# best_sentence_match_to_query:
# ['define global variable something with value bob']
# best_sentence_match_to_query:
# ['throw an error window in python in windows']
# best_sentence_match_to_query:
# ['beautifulsoup select div elements with an id attribute value ending with sub string in html parsed string soup']
# best_sentence_match_to_query:
# ['replace periods that are not followed by periods or spaces with period and space']

# query_ s = "beautifulsoup select div elements with an id attribute value ending with sub string in html parsed string soup"
# distances and indices:
# [[0.         0.01786615 0.01803862 0.01831566 0.0183698 ]]
# [[1386 1798   93 1210  926]]
# best_sentence_match_to_query:
# ['beautifulsoup', 'select', 'div', 'elements', 'with', 'an', 'id', 'attribute', 'value', 'ending', 'with', 'sub', 'string', 'in', 'html', 'parsed', 'string', 'soup']
# best_sentence_match_to_query:
# ['replace', 'occurrences', 'of', 'two', 'whitespaces', 'or', 'more', 'with', 'one', 'whitespace', 'in', 'string']
# best_sentence_match_to_query:
# ['get', 'all', 'digits', 'in', 'string', 'after', 'character']
# best_sentence_match_to_query:
# ['get', 'user', 'input', 'using', 'message', 'enter', 'name', 'here', 'and', 'insert', 'it', 'to', 'the', 'first', 'placeholder', 'in', 'string', 'hello', 'how', 'do', 'you', 'do']
# best_sentence_match_to_query:
# ['find', 'all', 'the', 'tags', 'and', 'div', 'from', 'beautiful', 'soup', 'object', 'soup']

# IT'S NOT WORKING? ... this is when not using gensim's "data cleaning" (gensim preprocess function)
# query: s = "beautifulsoup select div elements with an id attribute value ending with sub string in html parsed string soup"
# distances and indices:
# [[0.01117827 0.01166314 0.01297139 0.01381503 0.01386503]]
# [[1210 1586 2280  951 2282]]
# best_sentence_match_to_query:
# ['get', 'user', 'input', 'using', 'message', "'Enter", 'name', 'here:', "'", 'and', 'insert', 'it', 'to', 'the', 'first', 'placeholder', 'in', 'string', "'Hello,", '{0},', 'how', 'do', 'you', "do?'"]
# best_sentence_match_to_query:
# ['Format', 'string', '`hello', '{name},', 'how', 'are', 'you', '{name},', 'welcome', '{name}`', 'to', 'be', 'interspersed', 'by', '`name`', 'three', 'times,', 'specifying', 'the', 'value', 'as', '`john`', 'only', 'once']
# best_sentence_match_to_query:
# ['throw', 'a', 'ValueError', 'with', 'message', "'represents", 'a', 'hidden', 'bug,', 'do', 'not', 'catch', "this'"]
# best_sentence_match_to_query:
# ['find', 'all', 'substrings', 'in', '`mystring`', 'beginning', 'and', 'ending', 'with', 'square', 'brackets']
# best_sentence_match_to_query:
# ['throw', 'a', 'value', 'error', 'with', 'message', "'A", 'very', 'specific', 'bad', 'thing', "happened',", "'foo',", "'bar',", "'baz'"]

# using gensim's preprocess again: STRANGE HOW IT GETS NEW RESULTS FROM RUN TO RUN:
# distances and indices:
# [[0.         0.01398336 0.01531202 0.01684486 0.01806644]]
# [[1386 1798 2041 1210 1640]]
# best_sentence_match_to_query:
# ['beautifulsoup', 'select', 'div', 'elements', 'with', 'an', 'id', 'attribute', 'value', 'ending', 'with', 'sub', 'string', 'in', 'html', 'parsed', 'string', 'soup']
# best_sentence_match_to_query:
# ['replace', 'occurrences', 'of', 'two', 'whitespaces', 'or', 'more', 'with', 'one', 'whitespace', 'in', 'string']
# best_sentence_match_to_query:
# ['find', 'the', 'tag', 'in', 'html', 'root', 'which', 'starts', 'with', 'the', 'text', 'text', 'and', 'assign', 'it', 'to']
# best_sentence_match_to_query:
# ['get', 'user', 'input', 'using', 'message', 'enter', 'name', 'here', 'and', 'insert', 'it', 'to', 'the', 'first', 'placeholder', 'in', 'string', 'hello', 'how', 'do', 'you', 'do']
# best_sentence_match_to_query:
# ['find', 'all', 'owl', 'class', 'tags', 'by', 'parsing', 'xml', 'with', 'namespace']

# IT'S NOT JUNK, it's actually does retrieve the original sentence again
# it's just that the matches aren't that great when using
# ... this is when not using gensim's "data cleaning" (gensim preprocess function)
# distances and indices:
# [[0.00809363 0.01095894 0.01105138 0.01203837 0.01216143]]
# [[1386 2282 1586  297 2061]]
# best_sentence_match_to_query:
# ['BeautifulSoup', 'select', "'div'", 'elements', 'with', 'an', 'id', 'attribute', 'value', 'ending', 'with', 'sub-string', "'_answer'", 'in', 'HTML', 'parsed', 'string', '`soup`']
# best_sentence_match_to_query:
# ['throw', 'a', 'value', 'error', 'with', 'message', "'A", 'very', 'specific', 'bad', 'thing', "happened',", "'foo',", "'bar',", "'baz'"]
# best_sentence_match_to_query:
# ['Format', 'string', '`hello', '{name},', 'how', 'are', 'you', '{name},', 'welcome', '{name}`', 'to', 'be', 'interspersed', 'by', '`name`', 'three', 'times,', 'specifying', 'the', 'value', 'as', '`john`', 'only', 'once']
# best_sentence_match_to_query:
# ['Execute', 'a', 'put', 'request', 'to', 'the', 'url', '`url`']
# best_sentence_match_to_query:
# ['generate', 'a', 'random', 'number', 'in', '1', 'to', '7', 'with', 'a', 'given', 'distribution', '[0.1,', '0.05,', '0.05,', '0.2,', '0.4,', '0.2]']

# ----- it's not deterministic ....

# query is --> Decode Hex String in Python 3
# distances and indices:
# [[0.02282973 0.02311386 0.02355543 0.02372161 0.02372951]]
# [[1037 1870 2061 1386  951]]
#
# best_sentence_match_to_query:
# ['execute', 'sql', 'query', "'INSERT", 'INTO', 'table', "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'", 'with', 'all', 'parameters', 'in', 'list', '`tup`']
# best_sentence_match_to_query:
# ['throw', 'an', 'error', 'window', 'in', 'python', 'in', 'windows']
# best_sentence_match_to_query:
# ['generate', 'a', 'random', 'number', 'in', '1', 'to', '7', 'with', 'a', 'given', 'distribution', '[0.1,', '0.05,', '0.05,', '0.2,', '0.4,', '0.2]']
# best_sentence_match_to_query:
# ['BeautifulSoup', 'select', "'div'", 'elements', 'with', 'an', 'id', 'attribute', 'value', 'ending', 'with', 'sub-string', "'_answer'", 'in', 'HTML', 'parsed', 'string', '`soup`']
# best_sentence_match_to_query:
# ['find', 'all', 'substrings', 'in', '`mystring`', 'beginning', 'and', 'ending', 'with', 'square', 'brackets']
#
# Process finished with exit code 0

# query is --> Decode Hex String in Python 3
# distances and indices:
# [[0.03055988 0.03070806 0.03071547 0.03078923 0.03079331]]
# [[ 692 2061 2216 2282  700]]
#
# best_sentence_match_to_query:
# ['change', 'figure', 'size', 'to', '3', 'by', '4', 'in', 'matplotlib']
# best_sentence_match_to_query:
# ['generate', 'a', 'random', 'number', 'in', '1', 'to', '7', 'with', 'a', 'given', 'distribution', '[0.1,', '0.05,', '0.05,', '0.2,', '0.4,', '0.2]']
# best_sentence_match_to_query:
# ['shutdown', 'and', 'restart', 'a', 'computer', 'running', 'windows', 'from', 'script']
# best_sentence_match_to_query:
# ['throw', 'a', 'value', 'error', 'with', 'message', "'A", 'very', 'specific', 'bad', 'thing', "happened',", "'foo',", "'bar',", "'baz'"]
# best_sentence_match_to_query:
# ['Open', 'file', "'sample.json'", 'in', 'read', 'mode', 'with', 'encoding', 'of', "'utf-8-sig'"]
#
# Process finished with exit code 0

# query is --> Decode Hex String in Python 3
# distances and indices:
# [[0.0234028  0.02346684 0.0237515  0.02423743 0.02426082]]
# [[ 951 1870 1292  348 2151]]
#
# best_sentence_match_to_query:
# ['find', 'all', 'substrings', 'in', '`mystring`', 'beginning', 'and', 'ending', 'with', 'square', 'brackets']
# best_sentence_match_to_query:
# ['throw', 'an', 'error', 'window', 'in', 'python', 'in', 'windows']
# best_sentence_match_to_query:
# ['Find', 'all', '`div`', 'tags', 'whose', 'classes', 'has', 'the', 'value', '`comment-`', 'in', 'a', 'beautiful', 'soup', 'object', '`soup`']
# best_sentence_match_to_query:
# ['loop', 'through', '0', 'to', '10', 'with', 'step', '2']
# best_sentence_match_to_query:
# ['assign', 'value', 'in', '`group`', 'dynamically', 'to', 'class', 'property', '`attr`']
#
# Process finished with exit code 0

# query is --> How can I send a signal from a python program?
# distances and indices:
# [[0.04768149 0.04860793 0.04874119 0.04893681 0.04908829]]
# [[ 235 1280 1468  410 1403]]
#
# best_sentence_match_to_query:
# ['convert', 'a', 'string', '`s`', 'containing', 'a', 'decimal', 'to', 'an', 'integer']
# best_sentence_match_to_query:
# ['get', 'a', 'utf-8', 'string', 'literal', 'representation', 'of', 'byte', 'string', '`x`']
# best_sentence_match_to_query:
# ['decode', 'utf-8', 'code', '`x`', 'into', 'a', 'raw', 'unicode', 'literal']
# best_sentence_match_to_query:
# ['Convert', 'a', 'hex', 'string', '`437c2123', '`', 'according', 'to', 'ascii', 'value.']
# best_sentence_match_to_query:
# ['decode', 'JSON', 'string', '`u`', 'to', 'a', 'dictionary']

# query is --> How can I send a signal from a python program?
# distances and indices:
# [[0.04688263 0.04810128 0.04832134 0.04836203 0.04870835]]
# [[ 556 1331  509  936  162]]
# best_sentence_match_to_query:
# ['convert', 'a', 'beautiful', 'soup', 'html', '`soup`', 'to', 'text']
# best_sentence_match_to_query:
# ['call', 'a', 'function', '`otherfunc`', 'inside', 'a', 'bash', 'script', '`test.sh`', 'using', 'subprocess']
# best_sentence_match_to_query:
# ['extract', 'date', 'from', 'a', 'string', "'monkey", '2010-07-32', 'love', "banana'"]
# best_sentence_match_to_query:
# ['Print', 'a', 'emoji', 'from', 'a', 'string', '`\\\\ud83d\\\\ude4f`', 'having', 'surrogate', 'pairs']
# best_sentence_match_to_query:
# ['create', 'a', 'regular', 'expression', 'object', 'with', 'a', 'pattern', 'that', 'will', 'match', 'nothing']

# query is --> How can I send a signal from a python program?
# distances and indices:
# [[0.03736468 0.03764835 0.0380178  0.03809611 0.03824913]]
# [[1726  252  563  253 1468]]
# best_sentence_match_to_query:
# ['remove', 'all', 'spaces', 'from', 'a', 'string', 'converted', 'from', 'dictionary', "`{'a':", '1,', "'b':", "'as", "df'}`"]
# best_sentence_match_to_query:
# ['Remove', 'anything', 'in', 'parenthesis', 'from', 'string', '`item`', 'with', 'a', 'regex']
# best_sentence_match_to_query:
# ['create', 'a', 'set', 'from', 'string', '`s`', 'to', 'remove', 'duplicate', 'characters']
# best_sentence_match_to_query:
# ['Remove', 'word', 'characters', 'in', 'parenthesis', 'from', 'string', '`item`', 'with', 'a', 'regex']
# best_sentence_match_to_query:
# ['decode', 'utf-8', 'code', '`x`', 'into', 'a', 'raw', 'unicode', 'literal']


#------------------ with tf idf: -------------------

# query is --> How can I send a signal from a python program?
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.03502546 0.05633251 0.06268569 0.07116144 0.07517708]]
# [[1333 1394 2074  768 2185]]
# best_sentence_match_to_query:
# ---------> ['can', 'a', 'python', 'script', 'execut', 'a', 'function', 'insid', 'a', 'bash', 'script', '?']
# best_sentence_match_to_query:
# ---------> ['how', 'can', 'i', 'resiz', 'the', 'root', 'window', 'in', 'tkinter', '?']
# best_sentence_match_to_query:
# ['how', 'do', 'i', 'get', 'rid', 'of', 'python', 'tkinter', 'root', 'window', '?']
# best_sentence_match_to_query:
# ['execut', 'shell', 'script', 'from', 'python', 'with', 'variabl']
# best_sentence_match_to_query:
# ['how', 'can', 'i', 'launch', 'an', 'instanc', 'of', 'an', 'applic', 'use', 'python', '?']

# query is --> Decode Hex String in Python 3
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.08880949 0.10090542 0.10637978 0.10728473 0.10777972]]
# [[ 918 1528 1751  102    6]]
# best_sentence_match_to_query:
# ---------> ['python', ':', 'extract', 'number', 'from', 'a', 'string']
# best_sentence_match_to_query:
# ---------> ['un-escap', 'a', 'backslash-escap', 'string', 'in', '`', 'hello', ',', '\\\\nworld', '!', '`']
# best_sentence_match_to_query:
# ['revers', 'a', 'string', "'hello", 'world', "'"]
# best_sentence_match_to_query:
# ['trim', 'whitespac', 'in', 'string', '`', 's', '`']
# best_sentence_match_to_query:
# ['regex', 'for', 'repeat', 'word', 'in', 'a', 'string', '`', 's', '`']

# query is --> check if all elements in a list are identical
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.09066793 0.10030229 0.10454921 0.11992748 0.12080225]]
# [[2107 1274  761 1702 1589]]
# best_sentence_match_to_query:
# ---------> ['check', 'if', 'element', 'in', 'list', '`', 'my_list', '`', 'are', 'coher', 'in', 'order']
# best_sentence_match_to_query:
# ---------> ['check', 'if', 'all', 'element', 'in', 'list', '`', 'mylist', '`', 'are', 'the', 'same']
# best_sentence_match_to_query:
# ['delet', 'item', 'from', 'list', '`', 'my_list', '`', 'if', 'the', 'item', 'exist', 'in', 'list', '`', 'to_del', '`']
# best_sentence_match_to_query:
# ['creat', 'an', 'empti', 'list']
# best_sentence_match_to_query:
# ['check', 'if', 'ani', 'valu', 'in', 'a', 'list', '`', 'input_list', '`', 'is', 'a', 'list']

# query is --> Format string dynamically
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.10487765 0.10587065 0.10777695 0.11013259 0.110928  ]]
# [[1330 1772 1135  198  802]]
# best_sentence_match_to_query:
# ---------> ['custom', 'the', 'time', 'format', 'in', 'python', 'log']
# best_sentence_match_to_query:
# ---------> ['get', 'current', 'time', 'in', 'string', 'format']
# best_sentence_match_to_query:
# ['creat', 'a', 'symlink', 'directori', '`', 'd', ':', '\\\\testdirlink', '`', 'for', 'directori', '`', 'd', ':', '\\\\testdir', '`', 'with', 'unicod', 'support', 'use', 'ctype', 'librari']
# best_sentence_match_to_query:
# ['replac', 'special', 'charact', 'in', 'utf-8', 'encod', 'string', '`', 's', '`', 'use', 'the', '%', 'xx', 'escap']
# best_sentence_match_to_query:
# ['print', 'current', 'date', 'and', 'time', 'in', 'a', 'regular', 'format']

# query is --> How to convert a string from CP-1251 to UTF-8?
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.08822129 0.10125304 0.10413134 0.10791513 0.12609975]]
# [[ 430  585 2169   32 2100]]
# best_sentence_match_to_query:
# ---------> ['how', 'can', 'i', 'split', 'and', 'pars', 'a', 'string', 'in', 'python', '?']
# best_sentence_match_to_query:
# ---------> ['match', 'blank', 'line', 'in', '`', 's', '`', 'with', 'regular', 'express']
# best_sentence_match_to_query:
# ['un-escap', 'charact', 'in', 'a', 'string', 'with', 'python']
# best_sentence_match_to_query:
# ['find', 'the', 'string', 'match', 'within', 'parenthesi', 'from', 'a', 'string', '`', 's', '`', 'use', 'regex']
# best_sentence_match_to_query:
# ['split', 'string', "'happy_hats_for_cat", "'", 'use', 'string', "'_for_", "'"]

# query is --> How I can get rid of None values in dictionary?
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.09027725 0.13955621 0.14051476 0.14211081 0.1421888 ]]
# [[1139   95  205 2022 2099]]
# best_sentence_match_to_query:
# ---------> ['call', 'a', 'function', 'with', 'argument', 'list', '`', 'arg', '`']
# best_sentence_match_to_query:
# ---------> ['python', 'pickle/unpickl', 'a', 'list', 'to/from', 'a', 'file', "'afil", "'"]
# best_sentence_match_to_query:
# ['execut', 'shell', 'command', "'grep", '-r', 'pass', '*.log', '|', 'sort', '-u', '|', 'wc', '-l', "'", 'with', 'a', '|', 'pipe', 'in', 'it']
# best_sentence_match_to_query:
# ['print', 'all', 'environ', 'variabl']
# best_sentence_match_to_query:
# ['match', 'zero-or-mor', 'instanc', 'of', 'lower', 'case', 'alphabet', 'charact', 'in', 'a', 'string', '`', 'f233op', '`']

# query is --> Python: how to get the final output of multiple system commands?
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.04821762 0.05260197 0.07085422 0.07863148 0.0801897 ]]
# [[ 162  479  164 2057 2185]]
# best_sentence_match_to_query:
# ['regular', 'express', 'match', 'noth']
# best_sentence_match_to_query:
# ['save', 'json', 'output', 'from', 'a', 'url', '‘', 'http', ':', '//search.twitter.com/search.json', '?', 'q=hi', '’', 'to', 'file', '‘', 'hi.json', '’', 'in', 'python', '2']
# best_sentence_match_to_query:
# ['creat', 'a', 'regular', 'express', 'object', 'with', 'a', 'pattern', 'that', 'will', 'match', 'noth']
# best_sentence_match_to_query:
# ['how', 'to', 'use', 'variabl', 'in', 'sql', 'statement', 'in', 'python', '?']
# best_sentence_match_to_query:
# ['how', 'can', 'i', 'launch', 'an', 'instanc', 'of', 'an', 'applic', 'use', 'python', '?']

# query is --> splitting and concatenating a string
# positive_func is empty for sentence --> ['none']
# distances and indices:
# [[0.06805395 0.08449946 0.08764716 0.08858269 0.08987791]]
# [[ 563  986  759 1416  319]]
# best_sentence_match_to_query:
# ---> ['split', 'string', '`', 's', '`', 'into', 'string', 'of', 'repeat', 'element']
# best_sentence_match_to_query:
# ['split', 'string', '`', 'word', 'to', 'split', '`', 'into', 'a', 'list', 'of', 'charact']
# best_sentence_match_to_query:
# ['swap', 'each', 'pair', 'of', 'charact', 'in', 'string', '`', 's', '`']
# best_sentence_match_to_query:
# ['remov', 'first', 'word', 'in', 'string', '`', 's', '`']
# best_sentence_match_to_query:
# ['split', 'each', 'string', 'in', 'list', '`', 'mylist', '`', 'on', 'the', 'tab', 'charact']

# ---- retrieving code too: ----
# query is --> Finding the intersection between two series in Pandas
# distances and indices:
# [[0.3300746  0.3304731  0.33102885 0.33223322 0.33366433]]
# [[ 807  936 1233  808  806]]
# best_sentence_match_to_query:
# move x-axi to the top of a plot ` ax `
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code:
# ax.xaxis.tick_top()
# best_sentence_match_to_query:
# make a copi of list ` old_list `
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code:
# [i for i in old_list]
# best_sentence_match_to_query:
# select ` div ` tag whose ` id ` s begin with ` value_xxx_c_1_f_8_a_ `
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code:
# soup.select('div[id^="value_xxx_c_1_f_8_a_"]')
# best_sentence_match_to_query:
# move x-axi of the pyplot object ` ax ` to the top of a plot in matplotlib
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code:
# ax.xaxis.set_ticks_position('top')
# best_sentence_match_to_query:
# move an x-axi label to the top of a plot ` ax ` in matplotlib
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ corresponding code:
# ax.xaxis.set_label_position('top')
#
# Process finished with exit code 0








# queries
# query = "How can I define multidimensional arrays in python"
# query = "throw an error window in python in windows"
# query = "print variable value without spaces"   # really good matches
# query = "beautifulsoup select div elements with an id attribute value ending with sub string in html parsed string soup"
# query = "How can I send a signal from a python program?"
# query = "Decode Hex String in Python 3"
# query = "check if all elements in a list are identical"               # this one gives such great matches ...
# query = "Format string dynamically"
# query = "How to convert a string from CP-1251 to UTF-8?"
# query = "How I can get rid of None values in dictionary?"
# query = "Python: how to get the final output of multiple system commands?"
# query = "splitting and concatenating a string"
# query = "Finding the intersection between two series in Pandas"
# query = "Sending http headers with python"
# query = "Python -Remove Time from Datetime String"
# query = "How do I split a multi-line string into multiple lines?"
# query = "How to join mixed list (array) (with integers in it) in Python?"
# query = "Fastest way to get the first object from a queryset in django?"
#
