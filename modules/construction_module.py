from usr_func import get_parser_output_list, get_info_list_final, get_wx_words_dictionary, \
            get_wx_words_dictionary_new, get_wx_output_list, get_prune_output_list, get_root_word_dict_reverse
from concept_row_mod import get_row2

def get_row11(row_2,infoListFinal,wxWordsDictionary,rootWordDictReverse):
    conj_list = ["Ora", "waWA", "evaM"]
    disjunct_list = ["yA", "aWavA", "va"]
    final_result = []

    # for concept in row_2:
    for cc_item in (item for item in infoListFinal if item[1] == "CC"):
        cc_class_index = cc_item[2]
        cc_dependency = cc_item[3]
        cc_root_word = rootWordDictReverse.get(wxWordsDictionary.get(cc_item[0]))
        # print(cc_root_word)
        if cc_root_word is not None:
            const_list = []
            matching_values = [(value, index) for index, value in enumerate(infoListFinal)
                            if value[2] == cc_class_index and value[3] == cc_dependency and value[1] != "CC"]
            # print(matching_values)
            for value, _ in matching_values:
                cc_rel_root_word = rootWordDictReverse.get(wxWordsDictionary.get(value[0]))
                const_list.extend(index + 1 for index, element in enumerate(row_2) if cc_rel_root_word in element)
                # print(const_list)
            result_entry = None
            if cc_root_word in conj_list:
                result_entry = f"*conj:{const_list}"
            elif cc_root_word in disjunct_list:
                result_entry = f"*disjunct:{const_list}"

            if result_entry is not None:
                final_result.append(result_entry)

    if not final_result:
        final_result.append(" ")

    return final_result

if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    wxWordsDictionary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    parserOutputList=get_parser_output_list()
    pruneOutputList=get_prune_output_list()
    infoListFinal=get_info_list_final(parserOutputList)
    rootWordDictReverse=get_root_word_dict_reverse(pruneOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictionary)
    row_11=get_row11(row_2_result,infoListFinal,wxWordsDictionary,rootWordDictReverse)
    print(",".join(map(str,row_11)))