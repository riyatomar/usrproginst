from usr_func import *
from concept_row_mod import get_row2

#Row 6
def get_row2_index(word):
    # print("classword:",word)
    corr_index=0
    matched_concepts={}
    counter=1
    dep_list = ['rbks','rvks', 'k7', 'rh', '']
    for concept_final in row_2_result:
        temp_list=concept_final.split("+")
        matched_concepts[counter]=temp_list
        counter+=1
    # print(matched_concepts)
    #print(row_2)
    for key,value in matched_concepts.items():
        
        for root_words in value:
            if "-" in root_words:
                root_words=root_words.split("-")[0]
            if "_1" in root_words:
                root_words=root_words.strip("_1")
            if word==root_words:
                corr_index=key
                # print(corr_index)
            # print("matched word is:",root_words)
            # print("Correct index is:",key)
    if corr_index==0:
        for key,value in matched_concepts.items():
        
            for root_words in value:
                if "-" in root_words:
                    corr_index=key
    return corr_index

def get_row6(row_2):   
    #print("This is row_2:",row_2)
    #wx_word_inx=0
    row_6=[]
    row2_iter=[]#a list which is cleaned part of row2 to be worked upon
    row2_wx_index_iter=[]#list which has correct indexes of words in row_2
    class_word_index_list=[]#list which contains indexes of all class_words
    class_word_index_dict={}
    class_word_list=[]#list of class words from their indexexes in wx_format
    root_word_from_wx=[]#list of root words from their wx words
    dependency_col7_list=[]#list of col7 values in parser output
    correct_index_list=[]#list of final indexexs of dependencies in row2
    pos_tag_list=[]#list of pos tags of words present.
    #print(row_2)
    for concepts in row_2:
        if "+" in concepts:
            concepts=concepts.split("+")[1]
        if "-" in concepts:
            tam=concepts.split("-")[1].strip()
            concepts=concepts.split("-")[0]
            if tam == 'past':
                concepts = 'WA'
        concepts=concepts.split("_")[0]
        row2_iter.append(concepts)
        # print(row2_iter)
    # print("iterable:",row2_iter) #iterable after cleaning
    # print("root_word_dic",root_word_dict)
    for root_word in row2_iter:
        wx_word=rootWordDict.get(root_word)
        # print(wxWordsDictinaryNew)
        wx_word_inx=wxWordsDictinaryNew[wx_word]
        # print(wx_word_inx)
        #for key,value in temp_wx_words_dict.items():
         #   if value==wx_word:
          #      wx_word_inx=key
           #     value=0
        row2_wx_index_iter.append(wx_word_inx)
    
    
    # print("row2_wx_index:",row2_wx_index_iter) #indexes for same wx words
    
    for index_value in row2_wx_index_iter:
        par_value=parserOutputDict[index_value]
        class_word_index=int(par_value[6])
        pos_tag_value=par_value[3]
        dependency=par_value[7]
        class_word_index_list.append(class_word_index)
        dependency_col7_list.append(dependency)
        pos_tag_list.append(pos_tag_value)
    # print("class_word_indx_list:",class_word_index_list)
    # print("pos tag:",pos_tag_list)
    
    for index_6 in class_word_index_list:
        #do something about index_6==0 here
        if index_6==0:
            class_word_list.append(0)
        else:
            class_word_list.append(wxWordsDictinary[index_6])    
            
        # print(index_6)
    # print("This is class_word:",class_word_list)
    for word in class_word_list:
        if word==0:
            root_word_from_wx.append(0)
        else :
            key=rootWordDictReverse[word]
            root_word_from_wx.append(key)
    # print("root of that class:",root_word_from_wx)
    #Now we have to find,where this word is in row_2 and get that index
    for word in root_word_from_wx:
        if word==0:
            correct_index_list.append(0)
            continue
        correct_index=get_row2_index(word)
        # if correct_index=="0":

        # print("correct ind", correct_index)
        correct_index_list.append(correct_index)
    # print(correct_index_list)
    #print(dependency_col7_list)
    for val in range(len(dependency_col7_list)):
        if dependency_col7_list[val]=="main":
            row_6.insert(val,"0:main")
        else:
            #print(pos_tag_list[val])
            index_6a=str(correct_index_list[val])
            dependency_col7=dependency_col7_list[val]
            if  pos_tag_list[val]=="JJ":
                dependency_col7="mod"
            elif pos_tag_list[val]=="QC":
                dependency_col7="card"
            elif pos_tag_list[val]=="QO":
                dependency_col7="ord"
            elif dependency_col7=="lwg__neg":
                dependency_col7="neg"
            elif dependency_col7=="r6-k2":
                dependency_col7="k2"
            row_6.append(index_6a+":"+dependency_col7)
    #for word in row_6:
     #  if "r6-k2" in word:
      #  word.replace("r6-k2","r6")'''
    return row_6

if __name__=="__main__":
    wxOutputList=get_wx_output_list()
    parserOutputList=get_parser_output_list()
    wxWordsDictinary=get_wx_words_dictionary()
    wxWordsDictionaryNew=get_wx_words_dictionary_new()
    infoListFinal=get_info_list_final(parserOutputList)
    parserOutputDict=get_parser_output_dict()
    # rootWordDict=get_root_word_dict(pruneOutputList)
    # rootWordDictReverse=get_root_word_dict_reverse(pruneOutputList)

    row_2_result=get_row2(wxOutputList, wxWordsDictionaryNew, infoListFinal, wxWordsDictinary)
    row_6=get_row6(row_2_result)
    print(",".join(row_6))
    
