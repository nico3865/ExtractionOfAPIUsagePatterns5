
from CoNaLa.train_with_word2vec import get_dict_of_questions_and_code___not_stemmed_nor_tokenized
from CoNaLa.train_with_word2vec import tokenize
from CoNaLa.conala_eval import tokenize_for_bleu_eval


# # very small, but manually groomed corpus: (but the manually rewritten intents aren't that great actually, confusing stuff for word2vec and tf-idf with placeholderes etc -- raw English is better)
# input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-train.json"
# dict_of_questions_and_code = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False)

# bigger corpus:
input_file = "/Users/nicolasg-chausseau/Downloads/conala-corpus/conala-mined.jsonl.seq2seq"
dict_of_questions_and_code = get_dict_of_questions_and_code___not_stemmed_nor_tokenized(input_file, is_jsonl_binary_file=False)

SOquestions = []
for SOquestion in dict_of_questions_and_code.keys():
    SOquestion_toks = tokenize(SOquestion)
    SOquestions.append(SOquestion_toks)


SOcodes = []
for SOcode in dict_of_questions_and_code.values():
    SOcode_toks = tokenize_for_bleu_eval(SOcode)
    SOcodes.append(SOcode_toks)



import json
with open('encoder_inputs_for_transformer_BIG_ALL_FIXED.json', 'w') as outfile_encoder_inputs:
    json.dump(SOquestions, outfile_encoder_inputs)


with open('decoder_inputs_for_transformer_BIG_ALL_FIXED.json', 'w') as outfile_decoder_inputs:
    json.dump(SOcodes, outfile_decoder_inputs)






import keras
import numpy as np
from keras_transformer import get_custom_objects, get_model, decode



# -----
# read json:

# from google.colab import drive
# drive.mount('/content/drive')

from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(uploaded[fn])))


import json
with open('encoder_inputs_for_transformer_BIG.json') as json_file:
    SOquestions = json.load(json_file)

with open('decoder_inputs_for_transformer_BIG.json') as json_file:
    SOcodes = json.load(json_file)

# ----



# Build a small toy token dictionary
# tokens = 'I am testing the transformer architecture on google colab cloud a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z '.split(' ')
tokens = 'I am testing the transformer architecture on google colab cloud a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z '.split(' ')
token_dict = {
    '<PAD>': 0,
    '<START>': 1,
    '<END>': 2,
}

for sentence in SOquestions:
    for token in sentence:
        if token not in token_dict:
            token_dict[token] = len(token_dict)

for snippet in SOcodes:
    for token in snippet:
        if token not in token_dict:
            token_dict[token] = len(token_dict)

# this works fine:
# list_a = [0,1,2,3,4,5,6,7,8,9]
# list_b = list_a[-36:] # len(tokens)
# print(list_b)
encoder_inputs_no_padding = []
encoder_inputs = []
decoder_inputs = []
decoder_outputs = []
for i in range(0, len(SOquestions)):
    encode_tokens = SOquestions[i][:len(tokens)] # [:36] is to truncate the sentence at 36 words
    decode_tokens = SOcodes[i][-len(tokens):] # [:36] is to truncate the sentence at 36 words
    encode_tokens_NO_PADDING = ['<START>'] + encode_tokens + ['<END>']
    encode_tokens = ['<START>'] + encode_tokens + ['<END>'] + ['<PAD>'] * (len(tokens) - len(encode_tokens))
    output_tokens = decode_tokens + ['<END>', '<PAD>'] + ['<PAD>'] * (len(tokens) - len(decode_tokens))
    decode_tokens = ['<START>'] + decode_tokens + ['<END>'] + ['<PAD>'] * (len(tokens) - len(decode_tokens))
    encode_tokens = list(map(lambda x: token_dict[x], encode_tokens))
    decode_tokens = list(map(lambda x: token_dict[x], decode_tokens))
    output_tokens = list(map(lambda x: [token_dict[x]], output_tokens))
    encode_tokens_NO_PADDING = list(map(lambda x: token_dict[x], encode_tokens_NO_PADDING))
    encoder_inputs_no_padding.append(encode_tokens_NO_PADDING)
    encoder_inputs.append(encode_tokens)
    decoder_inputs.append(decode_tokens)
    decoder_outputs.append(output_tokens)


print(encoder_inputs)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(decoder_inputs)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(encoder_inputs_no_padding)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(decoder_outputs)







# and that's the old versio before testing it on google colab:

#
# # -----
# # read json:
#
# # from google.colab import drive
# # drive.mount('/content/drive')
#
#
# import json
# with open('encoder_inputs_for_transformer.json') as json_file:
#     SOquestions = json.load(json_file)
#
# with open('decoder_inputs_for_transformer.json') as json_file:
#     SOcodes = json.load(json_file)
#
# # ----
#
#
#
# # Build a small toy token dictionary
# tokens = 'I am testing the transformer architecture on google colab cloud'.split(' ')
# token_dict = {
#     '<PAD>': 0,
#     '<START>': 1,
#     '<END>': 2,
# }
#
# for sentence in SOquestions:
#     for token in sentence:
#         if token not in token_dict:
#             token_dict[token] = len(token_dict)
#
# for snippet in SOcodes:
#     for token in snippet:
#         if token not in token_dict:
#             token_dict[token] = len(token_dict)
#
# encoder_inputs_no_padding = []
# encoder_inputs = []
# decoder_inputs = []
# decoder_outputs = []
# for i in range(0, len(SOquestions)):
#     encode_tokens = SOquestions[i]
#     decode_tokens = SOcodes[i]
#     encode_tokens_NO_PADDING = ['<START>'] + encode_tokens + ['<END>']
#     encode_tokens = ['<START>'] + encode_tokens + ['<END>'] + ['<PAD>'] * (len(tokens) - len(encode_tokens))
#     output_tokens = decode_tokens + ['<END>', '<PAD>'] + ['<PAD>'] * (len(tokens) - len(decode_tokens))
#     decode_tokens = ['<START>'] + decode_tokens + ['<END>'] + ['<PAD>'] * (len(tokens) - len(decode_tokens))
#     encode_tokens = list(map(lambda x: token_dict[x], encode_tokens))
#     decode_tokens = list(map(lambda x: token_dict[x], decode_tokens))
#     output_tokens = list(map(lambda x: [token_dict[x]], output_tokens))
#     encoder_inputs_no_padding.append(encode_tokens_NO_PADDING)
#     encoder_inputs.append(encode_tokens)
#     decoder_inputs.append(decode_tokens)
#     decoder_outputs.append(output_tokens)
