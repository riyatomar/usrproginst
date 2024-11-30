from usr_func import get_prune_output_list, get_info_list_final, get_wx_output_list, \
            get_wx_words_dictionary, get_wx_words_dictionary_new, get_parser_output_list, get_NER_dict
from concept_row_mod import get_row2

def get_row4(row_2, pruneOutputList, nerDict):
    sem_category_list = []

    for concept in row_2:
        ner_val = ""
        for word, ner_tag in nerDict.items():
            if word in concept:
                if ner_tag == "B-PER":
                    ner_val = "per"
                elif ner_tag == "B-LOC":
                    ner_val = "loc"
                elif ner_tag in ["B-ORG", "I-ORG"]:
                    ner_val = "org"
                break
        
        # gender = ""
        # for item in pruneOutputList:
        #     gen_info = item.split()[3]
        #     if gen_info == 'f':
        #         gender = 'female'
        #         # print(gender)
        #     elif gen_info == 'm':
        #         gender = 'male'
        #     elif gen_info == 'unk':
        #         gender = ''

        
        sem_category_list.append(ner_val)

    return sem_category_list

if __name__=="__main__":
    pruneOutputList = get_prune_output_list()
    wxOutputList = get_wx_output_list()
    wxWordsDictinary = get_wx_words_dictionary()
    wxWordsDictionaryNew = get_wx_words_dictionary_new()
    parserOutputList = get_parser_output_list()
    infoListFinal = get_info_list_final(parserOutputList)
    nerDict = get_NER_dict()

    row_2_result = get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_4 = get_row4(row_2_result, pruneOutputList, nerDict)
    print(",".join(row_4))
