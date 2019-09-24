

# intellij doesn't find them but it runs fine.
from train_with_word2vec import get_BLEU_score_for_2_strings___CONALA_way
from train_with_word2vec import get_BLEU_score_for_2_strings___NLTK_way





# #import conala_eval why not found....
# get_BLEU_score_for_2_strings___CONALA_way(code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
# get_BLEU_score_for_2_strings___CONALA_way(english_query, corresponding_original_SOquestion, is_BLEU_for_code_evaluation_NOT_matchedQuery=False)
# print("bleu ntk for comparisno: ")
# get_BLEU_score_for_2_strings___NLTK_way(code, corresponding_code, is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
# get_BLEU_score_for_2_strings___NLTK_way(english_query, corresponding_original_SOquestion, is_BLEU_for_code_evaluation_NOT_matchedQuery=False)


print("========================================================================")
#import conala_eval why not found....
get_BLEU_score_for_2_strings___CONALA_way("print(x) for x in y", "print(x) for x in y", is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
get_BLEU_score_for_2_strings___CONALA_way("hello world how is it going?", "hello world how is it going?", is_BLEU_for_code_evaluation_NOT_matchedQuery=False)
print("bleu ntk for comparisno: ")
get_BLEU_score_for_2_strings___NLTK_way("print(x) for x in y", "print(x) for x in z", is_BLEU_for_code_evaluation_NOT_matchedQuery=True)
get_BLEU_score_for_2_strings___NLTK_way("hello world how is it going?", "hello warld how is it going?", is_BLEU_for_code_evaluation_NOT_matchedQuery=False)

