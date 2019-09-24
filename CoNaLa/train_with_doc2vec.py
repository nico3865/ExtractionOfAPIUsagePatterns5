# https://radimrehurek.com/gensim/models/doc2vec.html
import json

import gensim
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument



# very small, but manually groomed corpus:
# input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-train.json"   # MODIFY WHEN CHANGING CORPUS

# for json files:
def read_input_SMALL(input_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
        all_english_lines = []
        for p in data:
            line = p
            rewritten_intent = line["rewritten_intent"]
            # r_i_tokenized = word_tokenize(rewritten_intent)

            print()

            # do some pre-processing and return list of words for each review
            # text
            #yield gensim.utils.simple_preprocess(line)
            try:
                # x = gensim.utils.simple_preprocess(rewritten_intent)
                # TODO: check if it splits package.class.function correctly at the dots.
                # TODO: find another tokenizer, this one from gensim removes words like "multidimensional" ...
                x = rewritten_intent.split(" ")
                all_english_lines.append(x)
            except:
                continue
            print()

            # # from gensim.models import FastText
            # # # [...]
            # # sentences = SentencesIterator(tokens_generator)
            # # model = FastText(sentences)
    return all_english_lines



# a bit bigger:
input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-mined.jsonl"   # MODIFY WHEN CHANGING CORPUS

# for jsonl files:
def read_input_BIG(input_file):
    with open(input_file) as json_file:
        result = [json.loads(jline) for jline in json_file.readlines()]
        all_english_lines = []
        for p in result:
            line = p
            rewritten_intent = line["intent"]
            # r_i_tokenized = word_tokenize(rewritten_intent)

            # print()

            # do some pre-processing and return list of words for each review
            # text
            #yield gensim.utils.simple_preprocess(line)
            try:
                # x = gensim.utils.simple_preprocess(rewritten_intent)
                # TODO: check if it splits package.class.function correctly at the dots.
                x = rewritten_intent.split(" ")

                all_english_lines.append(x)
            except:
                continue
            # print()

            # # from gensim.models import FastText
            # # # [...]
            # # sentences = SentencesIterator(tokens_generator)
            # # model = FastText(sentences)
    return all_english_lines


# def getGenerator():
#     # [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]
#     for i, doc in enumerate(common_texts):
#         yield TaggedDocument(doc, [i])

# documents = getGenerator()
# documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(common_texts)]   # test with dummy corpus
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(read_input_BIG(input_file))]   # MODIFY WHEN CHANGING CORPUS
# documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(read_input_SMALL(input_file))]   # MODIFY WHEN CHANGING CORPUS

# model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)

# class TaggedDocumentIterator(object):
#     def __init__(self, doc_list, labels_list):
#         self.labels_list = labels_list
#         self.doc_list = doc_list
#     def __iter__(self):
#         for idx, doc in enumerate(self.doc_list):
#             # yield TaggedDocument(words=doc.split(), tags=[self.labels_list[idx]])
#             yield TaggedDocument(words=doc.split(), tags=idx)
#
# sentences = TaggedDocumentIterator(data, docLabels)

model = Doc2Vec(size=100, window=10, min_count=1, workers=11,alpha=0.025, iter=20)
model.build_vocab(documents)
print("model.corpus_count --> "+str(model.corpus_count))
print(documents[0])
print(documents[1])
print(documents[2])
print(documents[3])
print(documents[4])

# uncomment to retrain on new data, long:
model.train(documents, total_examples=model.corpus_count, epochs=model.iter)


# # persist a model to disk:
from gensim.test.utils import get_tmpfile
fname = get_tmpfile("my_doc2vec_model")   # MODIFY WHEN CHANGING CORPUS
# fname = get_tmpfile("my_doc2vec_model_SMALL")  # MODIFY WHEN CHANGING CORPUS
model.save(fname)
model = Doc2Vec.load(fname)  # you can continue training with the loaded model!


#

vector = model.infer_vector(["system", "response"])
print(vector)

# 1. Manos leaves the office every day at 18:00 to catch his train
# 2. This season is called Fall, because leaves fall from the trees.
# In a plain Word2Vec model the word would have exactly the same representation in both sentences, in Doc2Vec it will not.


# s1 = ["he","is","watching","TV"]
# s1 = common_texts[0]
# s1 = ["convert","list","to","string"]
# s1 = ["calculate","100","first","prime","numbers"]
# s = "How can I define multidimensional arrays in python"
# s = "print variable value without spaces"   # ?
# s = "beautifulsoup select div elements with an id attribute value ending with sub string in html parsed string soup"

s1 = s.split(" ")
# s1 = "trees"
print("input sentence --> "+str(s1))
# print(common_texts)

# get vector for sentence:
new_doc_vec = model.infer_vector(s1, steps=50, alpha=0.25)
# get the documents most similar to this one:
similars = model.docvecs.most_similar(positive=[new_doc_vec])
print("similars --> "+str(similars))
for x in range(0,5):
    try:
        #print(similars[x][0]) # need to train with the same dataset as used for query if testing :P
        most_similar_sentence = documents[int(similars[x][0])]
        print("most similar --> "+str(most_similar_sentence))
    except Exception as e:
        pass

# that's not good, it's for word2vecs ....
# most_similar = model.wv.most_similar(s1)
# print(most_similar)


# ---------------

# input sentence --> ['convert', 'list', 'to', 'string']
# similars --> [(66013, 0.7493085265159607), (354620, 0.7267504930496216), (371975, 0.7144357562065125), (35272, 0.7013987302780151), (360431, 0.6915557384490967), (48003, 0.6898911595344543), (165324, 0.6830461621284485), (496375, 0.6808695793151855), (431040, 0.6799755692481995), (550439, 0.6779723167419434)]
# most similar --> TaggedDocument(['convert', 'multi', 'dimensional', 'list', 'to', 'list', 'in', 'python'], [66013])
# most similar --> TaggedDocument(['convert', 'multi', 'dimensional', 'list', 'to', 'list', 'in', 'python'], [354620])
# most similar --> TaggedDocument(['convert', 'multi', 'dimensional', 'list', 'to', 'list', 'in', 'python'], [371975])
# most similar --> TaggedDocument(['convert', 'multi', 'dimensional', 'list', 'to', 'list', 'in', 'python'], [35272])
# most similar --> TaggedDocument(['convert', 'multi', 'dimensional', 'list', 'to', 'list', 'in', 'python'], [360431])


# input sentence --> ['calculate', '100', 'first', 'prime', 'numbers']
# similars --> [(527056, 0.8675168752670288), (425611, 0.8626860976219177), (127156, 0.8509724140167236), (535570, 0.8395540714263916), (227557, 0.8206844329833984), (477069, 0.8192093968391418), (258931, 0.8161647319793701), (33029, 0.8134804368019104), (572733, 0.8084330558776855), (466506, 0.8037289381027222)]
# most similar --> TaggedDocument(['in', 'python'], [527056])
# most similar --> TaggedDocument(['in', 'python'], [425611])
# most similar --> TaggedDocument(['python'], [127156])
# most similar --> TaggedDocument(['in', 'python'], [535570])
# most similar --> TaggedDocument(['python'], [227557])

# input sentence --> ['How', 'can', 'I', 'define', 'multidimensional', 'arrays', 'in', 'python']
# similars --> [(2473, 0.7738667130470276), (33110, 0.772879958152771), (98767, 0.7647101879119873), (116380, 0.752657949924469), (412550, 0.7369524240493774), (166691, 0.7119534015655518), (159524, 0.6846930384635925), (283040, 0.6814382076263428), (64204, 0.6741524934768677), (241029, 0.6665365695953369)]
# most similar --> TaggedDocument(['how', 'can', 'define', 'arrays', 'in', 'python'], [2473])
# most similar --> TaggedDocument(['how', 'can', 'define', 'arrays', 'in', 'python'], [33110])
# most similar --> TaggedDocument(['how', 'can', 'define', 'arrays', 'in', 'python'], [98767])
# most similar --> TaggedDocument(['how', 'can', 'define', 'arrays', 'in', 'python'], [116380])
# most similar --> TaggedDocument(['how', 'can', 'define', 'arrays', 'in', 'python'], [412550])

# when mismatch between sentence and dataset (sentence not in dataset:)
# input sentence --> ['print', 'variable', 'value', 'without', 'spaces']
# similars --> [(412126, 0.6368968486785889), (425470, 0.630292534828186), (39835, 0.6276929974555969), (13832, 0.6261231899261475), (244575, 0.5879048109054565), (234913, 0.5878573656082153), (407520, 0.5842467546463013), (469641, 0.5840834379196167), (54434, 0.5777673721313477), (325010, 0.577732503414154)]
# most similar --> TaggedDocument(['class', 'variable', 'vs', 'instance', 'variable', 'in', 'python', 'for', 'int', 'value'], [412126])
# most similar --> TaggedDocument(['class', 'variable', 'vs', 'instance', 'variable', 'in', 'python', 'for', 'int', 'value'], [425470])
# most similar --> TaggedDocument(['labeling', 'boxplot', 'in', 'seaborn', 'with', 'median', 'value'], [39835])
# most similar --> TaggedDocument(['convert', 'an', 'integer', 'to', 'byte', 'hex', 'value', 'in', 'python'], [13832])
# most similar --> TaggedDocument(['value', 'in', 'list', 'python'], [244575])

# # when sentence is in dataset: BAD!
# input sentence --> ['print', 'variable', 'value', 'without', 'spaces']
# similars --> [(884, 0.8140848278999329), (1471, 0.7983734607696533), (1073, 0.7855610847473145), (2276, 0.7800157070159912), (1609, 0.7791923880577087), (1940, 0.7618163824081421), (1606, 0.7592177391052246), (1847, 0.7544565796852112), (2128, 0.7487107515335083), (2260, 0.7450027465820312)]
# most similar --> TaggedDocument(['check', 'if', 'string', 'string', 'starts', 'with', 'number'], [884])
# most similar --> TaggedDocument(['check', 'whether', 'file', 'path', 'to', 'file', 'exists'], [1471])
# most similar --> TaggedDocument(['convert', 'an', 'int', 'to', 'hex', 'string'], [1073])
# most similar --> TaggedDocument(['substitute', 'occurrences', 'of', 'unicode', 'regex', 'pattern', 'with', 'empty', 'string', 'in', 'string', 'text'], [2276])
# most similar --> TaggedDocument(['print', 'unicode', 'string', 'text'], [1609])




# input sentence --> ['print', 'variable', 'value', 'without', 'spaces']
# similars --> [(106222, 0.6507468819618225), (228396, 0.6444957256317139), (518394, 0.6442152261734009), (234849, 0.624032735824585), (13675, 0.6232348680496216), (422539, 0.6192520260810852), (190022, 0.6151067018508911), (290186, 0.613852858543396), (161336, 0.6116672158241272), (14819, 0.6073604226112366)]
# most similar --> TaggedDocument(['print', 'the', 'value', 'of', 'a', 'variable', 'in', 'Python/Django?'], [106222])
# most similar --> TaggedDocument(['Adding', 'value', 'labels', 'on', 'a', 'matplotlib', 'bar', 'chart'], [228396])
# most similar --> TaggedDocument(['python', 'sort', 'list', 'of', 'json', 'by', 'value'], [518394])
# most similar --> TaggedDocument(['Remove', 'all', 'occurrences', 'of', 'a', 'value', 'from', 'a', 'Python', 'list'], [234849])
# most similar --> TaggedDocument(['Adding', 'value', 'labels', 'on', 'a', 'matplotlib', 'bar', 'chart'], [13675])



# NO NEED --> sklearn kneighbors algorithm

# TODO: IF NEEDED knn for very big datasets, not held in memory: build_from_doc2vec()
# TODO:  https://radimrehurek.com/gensim/similarities/index.html
# >>> indexer = AnnoyIndexer(model, 2)
# >>> model.most_similar("cat", topn=2, indexer=indexer)
# [('cat', 1.0), ('dog', 0.32011348009109497)]



