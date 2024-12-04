from usr_func import *

def word_search_from_end(search_word, rootWordDict, tamDictionaryList):
    # print(search_word)
    if "_1" in search_word:
        search_word=search_word.strip("_1")
        search_word=rootWordDict[search_word]
    #else:
     #   search_word=root_word_dict[search_word]
    #print("search_word:",search_word)
    match_key_list=[]
    matched_tams={}
    real_tam_search=search_word.strip()
    # print(tamDictionaryList)
    for line in tamDictionaryList:
        for value in line:
            if("pres"==value):
                print(line)
    #print("rtm in fn",real_tam_search)
    for line in tamDictionaryList:
        for value in line:
            if real_tam_search.endswith(value) and  value!="" :
                # print(line)
                # print("val:",value)
                key=value
                line0_length=len(line[0])
                # print(line[0])
                # print(line0_length)
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
    
# -------------------------------------------------------------------------------------------------------

def tam_rules(word,word_index,pof_check):
    # print(pof_check)
    ranjak_list= ["cala", "dAla", "cuka", "xe", "le", "bETa", "uTa", "jA", "padZa", "A"]
    temp_word_index=temp_word_index_iter=word_index+1
    temp_pos_tag=0
    vaux_count=0
    # print(temp_word_index)
    # print(infoListFinal[temp_word_index-1][1])
    while(infoListFinal[temp_word_index-1][1]=="VAUX"):
        vaux_count=vaux_count+1
        # print('vaux count-->', vaux_count)
        temp_word_index=temp_word_index+1
    # print(word)
    # print(rootWordDict)
    if(vaux_count==0):
        root_word=get_root_word(word, rootWordDictReverse)
        if(root_word=="hE" or root_word=="WA"):
            if(root_word=="hE"):
                final_word=root_word+"_1-pres"
            else:
                final_word="hE"+"_1-past"
            concept_list.append(final_word)
            return final_word
        else:
            personDictionary=get_person_dictionary()
            person_value=personDictionary[word]
            root_word=get_root_word(word, rootWordDictReverse)
            final_word=root_word+"_1-"+suffixDictionary[word]
    elif(vaux_count==1):
        word_index_in=temp_word_index_iter
        # print(word_index_in)
        vaux_word=wxOutputList[word_index_in-1]
        root_word=get_root_word(word, rootWordDictReverse)
        # print('root_word-->', root_word)
        vaux_root=get_root_word(vaux_word, rootWordDictReverse)
        # print('vaux_root-->', vaux_root)

        if(vaux_root=="jA" and suffixDictionary[word]=="yA"):
            final_word=root_word+"_1-"+suffixDictionary[word]+"_"+vaux_root+"_"+suffixDictionary[vaux_word]
        elif(vaux_root in ranjak_list):
            final_word=root_word+"_1-"+suffixDictionary[vaux_word]
        else:
            final_word=root_word+"_1-"+suffixDictionary[word]+"_"+vaux_word
    else:
        word_index_in=temp_word_index_iter
        vaux_word=wxOutputList[word_index_in-1]
        root_word=get_root_word(word, rootWordDictReverse)
        vaux_root=get_root_word(vaux_word, rootWordDictReverse)
        if(vaux_root=="jA" and suffixDictionary[word]=="yA"):
            if(suffixDictionary[vaux_word]=="0"):
                final_word=root_word+"_1-"+suffixDictionary[word]+"_"+vaux_root
            else:
                final_word=root_word+"_1-"+suffixDictionary[word]+"_"+vaux_root+"_"+suffixDictionary[vaux_word]
            temp_word_index_in=word_index_in
            while(infoListFinal[temp_word_index_in][1]=="VAUX"):
                temp_vaux=wxOutputList[temp_word_index_in]
                final_word=final_word+"_"+temp_vaux
                temp_word_index_in=temp_word_index_in+1
        elif(vaux_root in ranjak_list):
            final_word=root_word+"_1-"+suffixDictionary[vaux_word]
            temp_word_index_in=word_index_in
            while(infoListFinal[temp_word_index_in][1]=="VAUX"):
                temp_vaux=wxOutputList[temp_word_index_in]
                # print(temp_vaux)
                final_word=final_word+"_"+temp_vaux
                temp_word_index_in=temp_word_index_in+1
        else:
            final_word=root_word+"_1-"+suffixDictionary[word]
            temp_word_index_in=word_index_in-1
            while(infoListFinal[temp_word_index_in][1]=="VAUX"):
                temp_vaux=wxOutputList[temp_word_index_in]
                final_word=final_word+"_"+temp_vaux
                temp_word_index_in=temp_word_index_in+1
            
    final_word=final_word+"_1"

    if(vaux_count==0):
        if(suffixDictionary[word]=="imper" and person_value=="m_h"):
            final_word=final_word.rsplit('_',1)[0]
            final_word=final_word+"_o_2"
        elif(suffixDictionary[word]=="imper"):
            final_word=final_word.rsplit('_',1)[0]
            final_word=final_word+"_o_1"
        elif(suffixDictionary[word]=="subj"):
            final_word=final_word.rsplit('_',1)[0]
            final_word=final_word+"_e_1"
    elif(vaux_count>0):
        if(suffixDictionary[word]=="imper"):
            final_word=final_word.rsplit('_',1)[0]
            final_word=final_word+"_o_1"


    # print(infoListFinal)
    pof_index_check=-1
    for i in infoListFinal:
        if(i[2]==str(word_index) and i[3]=="pof"):
            pof_index_check=i[0]
            pof_word=wxOutputList[pof_index_check-1]
    if(pof_index_check==-1):
        concept_list.append(final_word)
        return final_word
    
    pof_result=pof_check[pof_word]
    # print(pof_result)
    # print(concept_list)
    if(pof_result in concept_list):
        replace_index=concept_list.index(pof_result)
        final_word=pof_result.split('+',-1)[0]+"+"+final_word
        concept_list[replace_index]=final_word
    # print(final_word)
    return final_word

# --------------------------------------------------------------------------------------------

def search_tam_row2(concept_list, rootWordDict, rootWordDictReverse, suffixDictionary):
    ranjak_list= ["cala", "dAla", "cuka", "xe", "le", "bETa", "uTa", "jA", "padZa", "A"]
    # print(concept_list)
    # print(suffixDictionary)
    tam_list_row2=identify_vb(concept_list)
    # if(len(tam_list_row2)==1):
    #     onlyvb=tam_list_row2[0]
        
    # print(tam_list_row2)
    # print("This is our vb:",tam_list_row2)
     
    for concept_with_hyphen in tam_list_row2:
        # print(tam_list_row2)
        #print("The verb group to be replaced:",concept_with_hyphen)
        #concept_with_hyphen is the word in concept list that we have to replace
        if concept_with_hyphen.split("-")[1]=="":
            
            real_tam_temp="0"
        else:
            real_tam_temp=concept_with_hyphen.split("-")[1]
        #print(real_tam_temp)
        if real_tam_temp=="0":
            root_concept=concept_with_hyphen.split("-")[0]
            # print(root_concept)
            #print("rc:",root_concept)
            search_word=root_concept.strip("_1")
            if "+" in root_concept:
                search_word=root_concept.split("+")[1]
            if "_1" in search_word:
                search_word=search_word.strip("_1")
            # print(search_word)
            search_word=rootWordDict[search_word]
            #print("sw in row2:",search_word)
            
            key_tam=word_search_from_end(search_word, rootWordDict, tamDictionaryList)
            # print(key_tam)
            # print("key_tam value in search_tam_row2:",key_tam)
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
    category_6=['jo', 'jahAZ', 'jisa', 'jaba', 'jina', 'jiwanA', 'jisakA', 'jisake']
    for index in range(len(concept_list_temp)):
        word=concept_list_temp[index]
        # print(word)
        if "+" in word:
            continue
        else:
            if word in category_1:
                concept_list_temp[index]="$addressee"
            elif word in category_2:
                concept_list_temp[index]="$speaker"
            elif word in category_3:
                concept_list_temp[index]="$respect"
            elif word in category_4:
                concept_list_temp[index]="$wyax"
            elif word.strip('_1') in category_5:
                concept_list_temp[index]="$kim"
            elif word.strip('_1') in category_6:
                concept_list_temp[index]="$yax"
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
        # print("temp",temp)
        already_visited[temp]=1
        final_word=rootWordDictReverse[word]+"+"+rootWordDictReverse[temp]
    else:
        final_word=word
    return final_word

def function1(concept_list):
    tam_details=[]
    with open("dictionaries/tam_dict.tsv","r") as tam_details_dict:
        tam_details=tam_details_dict.read().split("\n")
        # print(tam_details)
    for k in range(0,len(concept_list)):
        last_concept_list=concept_list[k]
        check_in_details=last_concept_list.rsplit("-",1)
        if(len(check_in_details)==2):
            for i in tam_details:
                each_detail=i.split("\t")
                for j in each_detail:
                    if(j==check_in_details[1]):
                        check_in_details[1]=each_detail[0]
        
            concept_list[k]=check_in_details[0]+"-"+check_in_details[1]

def get_row2(wxOutputList, wxWordsDictinaryNew, infoListFinal, wxWordsDictinary):
    ranjak_list= ["cala", "dAla", "cuka", "xe", "le", "bETa", "uTa", "jA", "padZa", "A"]
    plus_words = ['sAWa']
    pof_check={}
    counter=0
    temp_use={}
    ele_remove=''
    # print(pof_check)
    # print(wxOutputList)
    for i in range(len(wxOutputList)):
        word=wxOutputList[i]
        word_index=i+1 #word index of the word in wx_list
        for line in infoListFinal:
            if word_index in line:
                pos_tag=line[1]
                class_index=int(line[2])
                word_info=line[3]
        #main condition check begins here:
        # print(word,pos_tag)
        if pos_tag=="PSP"  or pos_tag=="SYM" or pos_tag=="CC" or pos_tag=="RP":
            continue
        
        if pos_tag == "NST" and wxWordsDictinary[word_index] in ('ora', 'sAWa') and wxWordsDictinary[word_index-1] in ('kI', 'kA', 'ke'):
            continue
                
        elif pos_tag=="VM" and word_info in ["main", "ccof", "rc"]: #Do not add suffix for these words because we have to do TAM search on them and it creates a problem later.
            # print(word)
            final_word=tam_rules(word,word_index,pof_check)

            VM_already_visited[word]=final_word #adding to the dictionary
            #sprint("this is final word:",final_word)
            pof_check[word]=final_word
        elif pos_tag=="VAUX" :
            if word in already_visited:
                if already_visited[word]==1:
                    continue
        elif pos_tag=="NNC" or word_info=="pof":
            if class_index in temp_use:
                concept_list.remove(temp_use[class_index]) 
                del temp_use[class_index]  
            final_word=for_handling_nnc_tag_or_pof(word,class_index,wxWordsDictionary,word_info)
            temp_use[class_index]=final_word
            concept_list.append(final_word)
            pof_check[word]=final_word
            # print(concept_list)
        elif pos_tag=="PRPC":
            final_word = for_handling_prpc(word, word_index, rootWordDictReverse, infoListFinal, wxWordsDictinary)
            concept_list.append(final_word)
            pof_check[word]=final_word
        else:
            if word in already_visited and word_index in already_visited.values():
                continue
            root_word=get_root_word(word, rootWordDictReverse)
            
            if pos_tag=="PRP" or pos_tag=="DEM" or pos_tag=="NNP" or pos_tag=="QC":
                key_to_check = wxWordsDictinary[word_index]
                if key_to_check in already_visited:
                    ele_remove=rootWordDictReverse[key_to_check]
                concept_list.append(root_word)
                if ele_remove is not None and ele_remove in concept_list:
                    concept_list.remove(ele_remove)
                pof_check[word]=root_word

                #Rule to add _1 in eka
                if key_to_check == 'eka':
                    root_word = root_word + '_1'
                    if 'eka' in concept_list: 
                        concept_list.remove('eka')
                    if root_word not in concept_list: 
                        concept_list.append(root_word)


            else:
                                       
                if(word_index not in already_visited):
                    # print(already_visited)
                    store_t=root_word+"_1"
                    with open('txt_files/measuring_units.txt','r') as file:
                        units=file.read()
                        units_list=units.split("\n")
                    if root_word in units_list:
                        if concept_list[-1].isdigit():
                            concept_list[-1]=concept_list[-1]+"+"+store_t
                    else:
                        concept_list.append(store_t)
                        pof_check[word]=store_t

                if root_word.strip() in plus_words:
                    store_t = root_word + "_1"
                    store_t_index = concept_list.index(store_t)
                    # print(store_t_index)
                    if store_t_index > 0:  
                        concept_list.append(concept_list[store_t_index - 1]+'+'+store_t)
                        # print(concept_list)
                        concept_list.remove(concept_list[store_t_index - 1])
                        concept_list.remove(store_t)
                        # print(concept_list)
                if root_word.endswith('nA') and pos_tag == 'VM':
                    root_to_remove = root_word + '_1'
                    updated_root_word = root_word[:-2]
                    matching_element = next((elem for elem in concept_list if root_to_remove in elem), None)
                    matching_element_list = matching_element.split('+')
                    
                    if '+' in matching_element:
                        if len(matching_element_list) == 2: 
                            verbalizer = matching_element_list[1]
                            kriyAmUla = matching_element_list[0]
                            concept_list.remove(kriyAmUla + '+' + verbalizer)
                            concept_list.append(kriyAmUla + '+' + updated_root_word + '_1')
                        elif len(matching_element_list) > 2:
                            verbalizer = matching_element_list[2]
                            kriyAmUla = matching_element_list[0] + '+' + matching_element_list[1]
                            concept_list.remove(kriyAmUla + '+' + verbalizer)
                            concept_list.append(kriyAmUla + '+' + updated_root_word + '_1')
                    else:
                        concept_list.remove(root_to_remove)
                        concept_list.append(updated_root_word + '_1')    
        counter+=1
        

    return concept_list
       
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
        personDictionary=get_person_dictionary()

        row_2=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
        
        function1(row_2)  # Call function1 with row_2
        row_2_temp=row_2.copy()
        row_2_chg=pronouns_n_qnwords_to_replace(row_2_temp)

        print(",".join(row_2_temp))

        concept_Row = []  # Assuming you have a list named concept_Row
        function1(concept_Row)  # Call function1 with concept_Row

