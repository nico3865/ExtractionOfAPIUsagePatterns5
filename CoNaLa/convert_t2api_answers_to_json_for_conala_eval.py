
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










# dict_of_questions_and_code = {}
import collections

with open("t2api_code2eng_output_for_conala_eval.txt") as line_file:

    answers_lines = line_file.readlines()

with open('T2API_CODE_2_ENG.test.json', 'w') as conala_test_file:
    json.dump(answers_lines, conala_test_file)
