from usr_func import *
from concept_row_mod import get_row2
from dependency_module import get_row6

# Row 10:Sentence type
def get_row10(row_2, wxOutputList):#, row_6):
    # main_true=False
    # for ele in row_6:
    #     dep_rel = ele.split(':')[1]
    #     dep_head = ele.split(':')[0]
    #     if dep_rel == "main":
    #         main_true=True
    #     if dep_rel == 'neg' and dep_head == 
    for ele in row_2:
        sentence_type = []
        if "nahI" in wxOutputList or "nahIM" in wxOutputList or "na" in wxOutputList or "manA" in wxOutputList:
            sentence_type.append('%negative')
        else:
            if "?" in wxOutputList:
                sentence_type.append("%interrogative")
            elif "|" in wxOutputList:
                sentence_type.append("%affirmative")
            elif "." in wxOutputList:
                sentence_type.append("%affirmative")
            elif "!" in wxOutputList:
                sentence_type.append("%exclamatory")
    # print(sentence_type)
    return sentence_type


if __name__ == "__main__":
    wxOutputList=get_wx_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    parserOutputList=get_parser_output_list()
    infoListFinal=get_info_list_final(parserOutputList)
    pruneOutputList=get_prune_output_list()
    parserOutputDict=get_parser_output_dict()
    rootWordDict=get_root_word_dict(pruneOutputList)
    rootWordDictReverse=get_root_word_dict_reverse(pruneOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    # row_6 = get_row6(row_2_result, wxWordsDictinary, wxWordsDictionaryNew, parserOutputDict, rootWordDict, rootWordDictReverse)
    row_10 = get_row10(row_2_result, wxOutputList)#, row_6)
    print(",".join(row_10))
