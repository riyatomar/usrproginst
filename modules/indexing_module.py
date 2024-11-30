from usr_func import get_parser_output_list, get_info_list_final, get_wx_words_dictionary, \
            get_wx_words_dictionary_new, get_wx_output_list
from concept_row_mod import get_row2

#Row 3 of USR:Index for concepts
def get_row3(concept_list):
    index_for_concepts=[]
    for ind in range(len(concept_list)):
        index_for_concepts.append(ind+1)
    return index_for_concepts
    

if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    parserOutputList=get_parser_output_list()
    infoListFinal=get_info_list_final(parserOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_3=get_row3(row_2_result)
    print(",".join(map(str,row_3)))