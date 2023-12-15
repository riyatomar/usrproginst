from usr_func import get_wx_output_list, get_wx_words_dictionary, get_wx_words_dictionary_new, \
    get_info_list_final, get_parser_output_list
from concept_row_module import get_row2

#row 9
def get_row_unk(row_2):
    comma_list=[]
    for x in range(len(row_2)):
        comma_list.append("")
    return comma_list 

if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    parserOutputList=get_parser_output_list()
    infoListFinal=get_info_list_final(parserOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_9=get_row_unk(row_2_result)
    print(",".join(row_9))