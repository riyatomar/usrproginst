from usr_func import get_wx_output_list, get_wx_words_dictionary, get_wx_words_dictionary_new, \
            get_info_list_final, get_parser_output_list, get_prune_output_list
from concept_row_module import get_row2

def get_row5(row_2, pruneOutputList):
    gnp_list_temp=[]
    row_5_temp=[]
    for concept in row_2:
        concept=concept.strip()
        #print(concept)
        if "+" in concept or "-" in concept or "_" in concept:
            #print("this:",concept)
            row_5_temp.append(",")
        else:
            row_5_temp.append(concept)
   
    for word in row_5_temp:
        if word==",":
            gnp_list_temp.append("")
        else:
            # gender="-"
            number="-"
            # person="-"
            for line in pruneOutputList:
                #print(line)
                if word == line.split(",")[2]:
                    #print("line",line)
                    number=line.split(",")[4]
                    if number=="s":
                        number="sg"
                    if number=="p":
                        number="pl"
                    if number=="unk":
                        number=""
            # gnp_list_temp.append("["+""+gender+" "+number+" "+person+"]")
            gnp_list_temp.append(number)
                    
    #print("gnp_list_temp:",gnp_list_temp)               
    return gnp_list_temp
   
if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    parserOutputList=get_parser_output_list()
    infoListFinal=get_info_list_final(parserOutputList)
    pruneOutputList=get_prune_output_list()

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_5 = get_row5(row_2_result, pruneOutputList)  
    print(",".join(map(str, row_5)))