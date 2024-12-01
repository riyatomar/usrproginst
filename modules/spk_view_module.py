from usr_func import get_wx_output_list, get_parser_output_list, get_wx_words_dictionary, \
        get_wx_words_dictionary_new, get_info_list_final, get_root_word_dict, get_prune_output_list, get_root_word_dict_reverse
from concept_row_mod import get_row2

#row 8
def get_row8(row_2, wxOutputList, wxWordsDictionary, 
            wxWordsDictionaryNew, infoListFinal, rootWordDict, rootWordDictReverse):
    
# Ranjak kriya infomation in 8th row
    ranjak_list = ["cala", "dAla", "cuka", "xe", "le", "bETa", "uTa", "jA", "padZa", "A"]
    complete_info = []
    # print(rootWordDictReverse)
    for concept in row_2:
        # print(row_2)
        if 'vaha' in concept:
            complete_info.append('distal')
            continue
        if 'yaha' in concept:
            complete_info.append('proximal')
            continue
        if "-" not in concept:
            complete_info.append('')
            continue
        for element in infoListFinal:
            if element[1] == 'VM' and element[3] == 'main':
                vm_next_idx = int(element[0]) + 1
                vm_next_word = wxWordsDictionary.get(vm_next_idx)
                if vm_next_word in ['.', '?', '|']:
                    complete_info.append('')
                    continue
                
                vm_next_root = rootWordDictReverse.get(vm_next_word)
                if not vm_next_root:
                    complete_info.append('')
                    continue
                
                for item in infoListFinal:
                    if item[0] == vm_next_idx and item[1] == "VAUX":
                        complete_info.append("["+""+"shade"+":"+vm_next_root+"_1"+"]" if vm_next_root in ranjak_list else '')
                        break
                else:
                    complete_info.append('')


# Discourse particle information in 8th row
    for word in wxOutputList:
        word_index=wxWordsDictionaryNew[word]
        # print(wxWordsDictionary)
        for line in infoListFinal:
            if word_index in line:
                pos_tag=line[1]
                class_index=line[2]
                if pos_tag=="RP":
                    rp_root_word=rootWordDict[word]
                    # print(rp_root_word)
                    rp_class_index = class_index
                    rp_class_index_word = wxWordsDictionary[int(rp_class_index)]
                    row_2 = [word.rstrip("_1") for word in row_2]
                    rp_rel_word_index = row_2.index(rootWordDictReverse[rp_class_index_word])
                    # rp_rel_word_index = row_2.index(rp_class_index_word)
                    # complete_info[rp_rel_word_index]=rp_root_word
                    # complete_info[rp_rel_word_index]+= " " + rp_root_word
                    rp_existing_value = complete_info[rp_rel_word_index]
                    if rp_existing_value:
                        complete_info[rp_rel_word_index] += "/" + rp_root_word
                    
                    else:
                        complete_info[rp_rel_word_index] = rp_root_word

    return complete_info

if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    parserOutputList=get_parser_output_list()
    wxWordsDictionary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    pruneOutputList=get_prune_output_list()
    infoListFinal=get_info_list_final(parserOutputList)
    rootWordDict=get_root_word_dict(pruneOutputList)
    rootWordDictReverse=get_root_word_dict_reverse(pruneOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictionary)
    row_8=get_row8(row_2_result, wxOutputList, wxWordsDictionary,
                   wxWordsDictionaryNew, infoListFinal, rootWordDict, rootWordDictReverse)
    print(",".join(row_8))