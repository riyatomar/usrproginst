from usr_func import get_wx_output_list, get_parser_output_list, get_wx_words_dictionary, \
        get_wx_words_dictionary_new, get_info_list_final, get_root_word_dict, get_prune_output_list
from concepts import get_row2

#row 8
def get_row8(row_2, wxOutputList, parserOutputList, wxWordsDictinary, 
            wxWordsDictionaryNew, infoListFinal, rootWordDict):
    
# Ranjak kriya infomation in 8th row
    ranjak_list = ["cala", "dAla", "cuka", "xe", "le", "bETa", "uTa", "jA", "padZa", "A"]
    complete_info = []

    for concept in row_2:
        if "-" in concept:
            
            for element in parserOutputList:
                pos = element[4]
                index = element[0]
                word_rel = element[7]
                word = element[1]
            
                if pos == "VM" and word_rel == "main":    
                    word = wxWordsDictinary[int(index)]
                    # print(word)
                    vm_next = int(index)+1
                    vm_next_word = wxWordsDictinary[vm_next]
                    # print(vm_next_word)
                    vm_next_ele = parserOutputList[vm_next-1]
                    # print(vm_next_ele)
                    vm_next_tag = vm_next_ele[4]
                    # print(vm_next_tag)

                    if vm_next_tag == "VAUX":
                        for tag in parserOutputList:
                            # print(tag)
                            word_val = tag  #.split(',')
                            # print(word_val)
                            if vm_next_word == word_val[1]:
                                # print(word_val[2])
                                if word_val[2] in ranjak_list:
                                    # print(word_val[2]) # [shade:xe_1]
                                    complete_info.append("["+""+"shade"+":"+word_val[2]+"_1"+"]")     
                    else:
                        complete_info.append("")                                                                                    
        else:
            complete_info.append("")

# Discourse particle information in 8th row
    for word in wxOutputList:
        word_index=wxWordsDictionaryNew[word]
        # print(wxWordsDictinary)
        for line in infoListFinal:
            if word_index in line:
                pos_tag=line[1]
                class_index=line[2]
                original_index=line[0]
                if pos_tag=="RP":
                    rp_root_word=rootWordDict[word]
                    # print(rp_root_word)
                    rp_class_index = class_index
                    rp_class_index_word = wxWordsDictinary[int(rp_class_index)]
                    # print(rp_class_index_word)
                    row_2 = [word.rstrip("_1") for word in row_2]
                    # print(row_2)
                    rp_rel_word_index = row_2.index(rp_class_index_word)
                    # complete_info[rp_rel_word_index]=rp_root_word
                    # complete_info[rp_rel_word_index]+= " " + rp_root_word
                    rp_existing_value = complete_info[rp_rel_word_index]
                    if rp_existing_value:
                        complete_info[rp_rel_word_index] += " " + rp_root_word
                    
                    else:
                        complete_info[rp_rel_word_index] = rp_root_word

    return complete_info

if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    parserOutputList=get_parser_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    pruneOutputList=get_prune_output_list()
    infoListFinal=get_info_list_final(parserOutputList)
    rootWordDict=get_root_word_dict(pruneOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_8=get_row8(row_2_result, wxOutputList, parserOutputList, wxWordsDictinary,
                   wxWordsDictionaryNew, infoListFinal, rootWordDict)
    print(",".join(row_8))