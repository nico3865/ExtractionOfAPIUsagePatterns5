
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




IS_USING_SMALL_ANNOTATED_CORPUS_ONLY = True #False

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

    conala_test_data_new_REVERSE = []
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

        p_new = {}
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
            line_snippet = line["snippet"]


            p_new["snippet"] = rewritten_intent
            p_new["rewritten_intent"] = line_snippet
            p_new["intent"] = line_snippet
            p_new["question_id"] = line["question_id"]
            conala_test_data_new_REVERSE.append(p_new.copy())

    with open('conala-test-REVERSE.json', 'w') as reverse_test_file:
        json.dump(conala_test_data_new_REVERSE, reverse_test_file)
        #transl_answers_file.write(dict_of_questions_and_code_TRAIN.values().totsring())
        # for sentence in dict_of_questions_and_code_TRAIN.values():
        #     sentence = sentence.replace('\n', ' ').replace('\r', '')
        #     transl_answers_file.write(sentence+"\n")

    #return dict_of_questions_and_code




print()
# ----------------------------------------------------- pick a corpus ---------------------------------------------------------
print()


input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-test.json"
get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False, isForReferenceFile=False)

# for key, value in dict_of_questions_and_code_TRAIN.items():
#     print(key +" --> "+value)
# sys.exit()

print()
# ----------------------------------------------------- /pick a corpus ---------------------------------------------------------
print()


# write to files for t2api berkeley aligner format: just two aligned text files -- line per line parallele corpus in two files
# for key, value in dict_of_questions_and_code_TRAIN:

#
# with open('train.cd', 'w') as transl_answers_file:
#     #json.dump(dict_of_questions_and_code_TRAIN.keys, outfile_results_conala_eval)
#     #transl_answers_file.write(dict_of_questions_and_code_TRAIN.values().totsring())
#     for sentence in dict_of_questions_and_code_TRAIN.values():
#         sentence = sentence.replace('\n', ' ').replace('\r', '')
#         transl_answers_file.write(sentence+"\n")
# with open('train.ts', 'w') as transl_input_file:
#     #json.dump(dict_of_questions_and_code_TRAIN.values, transl_input_file)
#     #transl_input_file.write(dict_of_questions_and_code_TRAIN.keys().tostring())
#     for sentence in dict_of_questions_and_code_TRAIN.keys():
#         sentence = sentence.replace('\n', ' ').replace('\r', '')
#         transl_input_file.write(sentence+"\n")
#
#
#
#
# # now again for test set:
# test_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-test.json"
# dict_of_questions_and_code_TEST = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(test_file, is_jsonl_binary_file=False)
#
# with open('tune.cd', 'w') as transl_answers_file:
#     #json.dump(dict_of_questions_and_code_TRAIN.keys, outfile_results_conala_eval)
#     #transl_answers_file.write(dict_of_questions_and_code_TRAIN.values().totsring())
#     for sentence in dict_of_questions_and_code_TEST.values():
#         sentence = sentence.replace('\n', ' ').replace('\r', '')
#         transl_answers_file.write(sentence+"\n")
# with open('tune.ts', 'w') as transl_input_file:
#     #json.dump(dict_of_questions_and_code_TRAIN.values, transl_input_file)
#     #transl_input_file.write(dict_of_questions_and_code_TRAIN.keys().tostring())
#     for sentence in dict_of_questions_and_code_TEST.keys():
#         sentence = sentence.replace('\n', ' ').replace('\r', '')
#         transl_input_file.write(sentence+"\n")

