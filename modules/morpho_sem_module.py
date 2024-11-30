from usr_func import get_wx_output_list, get_wx_words_dictionary, get_wx_words_dictionary_new, \
            get_info_list_final, get_parser_output_list, get_prune_output_list
from concept_row_mod import get_row2

def get_row5(row_2, pruneOutputList):
    gnp_list = []
    for concept in row_2:
        number = ""
        if "+" in concept or "-" in concept:
            number = ""
        else:
            for line in pruneOutputList:
                morph_info = line.split("\t")
                word = morph_info[2].strip()
                num = morph_info[4].strip()
                if word in concept:
                    if num == "p":
                        number = "pl"
                    if num == 'sg' or num == 'unk':
                        number = ""
        gnp_list.append(number)
    return gnp_list

if __name__ == "__main__":
    wxOutputList = get_wx_output_list()
    wxWordsDictinary = get_wx_words_dictionary()
    wxWordsDictionaryNew = get_wx_words_dictionary_new()
    parserOutputList = get_parser_output_list()
    infoListFinal = get_info_list_final(parserOutputList)
    pruneOutputList = get_prune_output_list()

    row_2_result = get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_5 = get_row5(row_2_result, pruneOutputList)  
    print(",".join(map(str, row_5)))
