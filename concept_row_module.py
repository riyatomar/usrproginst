from usr_func import *

def word_search_from_end(search_word, rootWordDict, tamDictionaryList):
    
    if "_1" in search_word:
        search_word=search_word.strip("_1")
        search_word=rootWordDict[search_word]
    #else:
     #   search_word=root_word_dict[search_word]
    #print("search_word:",search_word)
    match_key_list=[]
    matched_tams={}
    real_tam_search=search_word.strip()
    #print("rtm in fn",real_tam_search)
    for line in tamDictionaryList:
        
        for value in line:
            if real_tam_search.endswith(value) and  value!="" :
                #print("val:",value)
                key=value
                line0_length=len(line[0])
                if key not in matched_tams.keys():
                    matched_tams[value]=line[0]
                else:
                    if line0_length > len(matched_tams[value]):
                        matched_tams[value]=line[0]
    longest_key=int(0)
    longest_key_value=int(0)
    key_tam=None
    for key in matched_tams:
        key_temp_length=len(key)
        if key_temp_length>longest_key:
            longest_key_value=key
            longest_key=key_temp_length
    try:
        if longest_key_value !=0:
            key_tam=matched_tams[longest_key_value]
    
        
        # print("kt",key_tam)
    #key_tam is the value of longest matched TAM from TAM dictionary.
        return key_tam
    except Exception as e:
        print(e)
    
   

def search_tam_row2(concept_list, rootWordDict, rootWordDictReverse, suffixDictionary):
    ranjak_list= ["cala", "dAla", "cuka", "xe", "le", "bETa", "uTa", "jA", "padZa", "A"]
    tam_list_row2=identify_vb(concept_list)
    #print("This is our vb:",tam_list_row2)
     
    for concept_with_hyphen in tam_list_row2:
        #print("The verb group to be replaced:",concept_with_hyphen)
        #concept_with_hyphen is the word in concept list that we have to replace
        if concept_with_hyphen.split("-")[1]=="":
            
            real_tam_temp="0"
        else:
            real_tam_temp=concept_with_hyphen.split("-")[1]
        #print(real_tam_temp)
        if real_tam_temp=="0":
            root_concept=concept_with_hyphen.split("-")[0]
            #print("rc:",root_concept)
            search_word=root_concept.strip("_1")
            if "+" in root_concept:
                search_word=root_concept.split("+")[1]
            if "_1" in search_word:
                search_word=search_word.strip("_1")
            search_word=rootWordDict[search_word]
            #print("sw in row2:",search_word)
            
            key_tam=word_search_from_end(search_word, rootWordDict, tamDictionaryList)
            #print("key_tam value in search_tam_row2:",key_tam)
            if key_tam !=None:
                final_concept=root_concept+"-"+key_tam
            else:
                final_concept=root_concept
            #print(final_concept)
        else:
            #Word after hyphen in verb group
            root_concept=concept_with_hyphen.split("-")[0] 
            #Word before hyphen in verb group
            #print("root_concept:",root_concept)
            root_concept=root_concept.strip("_1")
            if "+" in root_concept:
                root_concept=root_concept.split("+")[1]
            if "_1" in root_concept:
                root_concept=root_concept.strip("_1")
            wx_word_for_root_concept=rootWordDict[root_concept]
            #this is the original word for root_concept
            #print(wx_word_for_root_concept)
            #real_tam_temp=real_tam_temp.strip("_")
            for char in real_tam_temp:
                if char=="_":
                    real_tam_temp=real_tam_temp.replace(char," ")
            #print("real_tam_temp",real_tam_temp)
            
            ranjak_search_vaux=real_tam_temp.split()[0]
            #print("rsv",ranjak_search_vaux)
            add_to_vaux=""
            # add_to_vaux=real_tam_temp.split()[1]
            # print(add_to_vaux)
            try:
                add_to_vaux=real_tam_temp.split()[1:]
            except:
                pass
            root_of_ranjak_search_vaux=rootWordDictReverse[ranjak_search_vaux.strip()]
            if root_of_ranjak_search_vaux in ranjak_list:
                real_tam_temp=rootWordDict[root_of_ranjak_search_vaux]
                real_tam_temp=suffixDictionary[real_tam_temp.strip()]+" "+" ".join(add_to_vaux)
            else:  
                real_tam_temp=ranjak_search_vaux+" "+" ".join(add_to_vaux)
            #print("rtm",real_tam_temp)
            real_tam_search=wx_word_for_root_concept+" "+real_tam_temp
            #if "_" in real_tam_search:
            #    real_tam_search=real_tam_search.strip("_")
            #print("real tam search_2:",real_tam_search) #This is the real TAM that we work with,searching in the backend happens on this.
            key_tam=word_search_from_end(real_tam_search, rootWordDict, tamDictionaryList)
            #print("key_tam",key_tam)
            #The above function,returns the actual TAM matching from the TAM dictionary
            #if no match found in TAM dictionary,it returns none.
            #print("print key_tam is:",key_tam)
            #concept_list=list(map(lambda x:x.replace(concept_with_hyphen,key_tam),concept_list))
            init_part=concept_with_hyphen.split("-")[0]
            if key_tam is not None:
                final_concept=init_part+"-"+key_tam
            else:
                final_concept=init_part
        #print("final concept:",final_concept)
        #print("This is the final concept:",final_concept)
        concept_list=list(map(lambda x:x.replace(concept_with_hyphen,final_concept),concept_list))
        #print(concept_list)
        
    return concept_list
#----------------------------------------------------------------------
def pronouns_n_qnwords_to_replace(concept_list):
    concept_list_temp=concept_list
    category_1=["wuma","wumhArA","wumako","wuJe","wU","wuJako","Apa"]
    category_2=["mEM","hama","hamArA","hamako","hameM","muJe","muJako"]
    category_3=["Ji"]
    category_4=["vaha","yaha"]
    category_5=["kyA","kOna","kaba","kahAz","kEse","kisase","kEsA","kyoM","kisane","kisako","kisaki","kiwanA","kiwanI","kisaliye"]
    for index in range(len(concept_list_temp)):
        word=concept_list_temp[index]
        if "+" in word:
            continue
        else:
            if word in category_1:
                concept_list_temp[index]="addressee"
            elif word in category_2:
                concept_list_temp[index]="speaker"
            elif word in category_3:
                concept_list_temp[index]="respect"
            elif word in category_4:
                concept_list_temp[index]="wyax"
            elif word in category_5:
                concept_list_temp[index]="kim"
            else:
                continue
    return concept_list_temp
#----------------------------------------------------------------------------------------------------------
def for_handling_prpc(word,word_index, rootWordDictReverse, infoListFinal, wxWordsDictinary):
    #print("wi",word_index)
    line= infoListFinal[word_index] #updated simply vaux to vaux root
    #print("line",line)
    pos_tag=line[1]
    if pos_tag=="PRP":
        word_index=line[0]
        temp=wxWordsDictinary[word_index]
        #print("temp",temp)
        already_visited[temp]=1
        final_word=rootWordDictReverse[word]+"+"+rootWordDictReverse[temp]
    else:
        final_word=word
    return final_word

    

def get_row2(wxOutputList, wxWordsDictinaryNew, infoListFinal, wxWordsDictinary):
    counter=0
    temp_use={}
    for i in range(len(wxOutputList)):
        word=wxOutputList[i]
        word_index=i+1 #word index of the word in wx_list
        for line in infoListFinal:
            if word_index in line:
                pos_tag=line[1]
                class_index=int(line[2])
                word_info=line[3]
        #main condition check begins here:
        
        if pos_tag=="PSP"  or pos_tag=="SYM" or pos_tag=="CC" or pos_tag=="RP":
            continue
        elif pos_tag=="VM" and word_info=="main": #Do not add suffix for these words because we have to do TAM search on them and it creates a problem later.
            
            root_word=get_root_word(word, rootWordDictReverse)
            vector_8th=get_8th_vector(word, suffixDictionary) 
            if word in VM_already_visited:
                
                root_word=VM_already_visited[word]
                concept_list.remove(root_word)

                final_word=root_word+"-"
            else:
                final_word=root_word+"_1"+"-"
            
            
            
            for line in infoListFinal[word_index:-1]: #updated simply vaux to vaux root
                pos_tag=line[1]
                if pos_tag=="VAUX":
                    word_index=line[0]
                    temp=wxWordsDictinary[word_index]
                    #temp_root=root_word_dict_reverse[temp]
                    final_word=final_word+"_"+temp
                    already_visited[temp]=1
                else:
                    break
            
            VM_already_visited[word]=final_word #adding to the dictionary
            #sprint("this is final word:",final_word)
            concept_list.append(final_word)
        elif pos_tag=="VAUX" :
            if word in already_visited:
                if already_visited[word]==1:
                    continue
            else:
                root_word=get_root_word(word, rootWordDictReverse)
                concept_list.append(root_word+"_1")
        elif pos_tag=="NNC" or word_info=="pof":
            if class_index in temp_use:
                concept_list.remove(temp_use[class_index]) 
                del temp_use[class_index]  
            final_word=for_handling_nnc_tag_or_pof(word,class_index,wxWordsDictionary,word_info)
            temp_use[class_index]=final_word
            concept_list.append(final_word)
        elif pos_tag=="PRPC":
            final_word=for_handling_prpc(word,word_index)
            concept_list.append(final_word)
        else:
            if word in already_visited and word_index in already_visited.values():
                continue
            root_word=get_root_word(word, rootWordDictReverse)
            
            if pos_tag=="PRP" or pos_tag=="DEM" or pos_tag=="NNP" or pos_tag=="QC":
                concept_list.append(root_word)
            else:
                if(word_index not in already_visited):
                    concept_list.append(root_word+"_1")
            
            
        counter+=1
    
    concept_list_final=search_tam_row2(concept_list, rootWordDict, rootWordDictReverse, suffixDictionary)
    #print("concept list final:",concept_list_final)
    return concept_list_final


if __name__=="__main__":
        
        wxOutputList=get_wx_output_list()
        parserOutputList=get_parser_output_list()
        wxWordsDictinary=get_wx_words_dictionary()
        wxWordsDictionaryNew=get_wx_words_dictionary_new()
        infoListFinal=get_info_list_final(parserOutputList)
        rootWordDict=get_root_word_dict(pruneOutputList)
        rootWordDictReverse=get_root_word_dict_reverse(pruneOutputList)
        tamDictionaryList=get_TAM_dictionary_list()
        suffixDictionary=get_suffix_dictionary()

        row_2=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
        row_2_temp=row_2.copy()
        row_2_chg=pronouns_n_qnwords_to_replace(row_2_temp)

        print(",".join(row_2_temp))

       


