from usr_func import get_prune_output_list, get_info_list_final, get_wx_output_list, \
            get_wx_words_dictionary, get_wx_words_dictionary_new, get_parser_output_list, get_NER_dict
from concept_row_module import get_row2

#row 4
def get_row4(row_2, pruneOutputList, nerDict):

    sem_category_list=[]
    if len(nerDict)==0:
        for concept in row_2:
            #print(concept)
            sem_category_list.append("")
    else:
        for concept in row_2:
            flag=0
            for word in nerDict:
                if word in concept:
                    flag=1
                    if nerDict[word] =="B-PER":
                        ner_val="per"
                    elif nerDict[word]=="B-LOC":
                        ner_val="loc"
                    elif nerDict[word]=="B-ORG" or nerDict[word]=="I-ORG":
                        ner_val="org"
                    sem_category_list.append(ner_val)
            if flag==0:
                sem_category_list.append("")
    

    
    
    return sem_category_list


if __name__=="__main__":
    pruneOutputList=get_prune_output_list()
    wxOutputList=get_wx_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    parserOutputList=get_parser_output_list()
    infoListFinal=get_info_list_final(parserOutputList)
    nerDict=get_NER_dict()

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_4=get_row4(row_2_result, pruneOutputList, nerDict)
    print(",".join(row_4))
