parser_file_input="txt_files/parser-output.txt"
prune_file_input="txt_files/prune-output.txt"
wx_file_input="txt_files/wx.txt"
ner_file_input="txt_files/ner_output"
# concept_dictionary_input="H_concept-to-mrs-rels.dat"

#===========================================================
def get_parser_output_list():
#Open the parser file,and store its contents into a 2d-list
    parser_output_list=[]
    with open(parser_file_input,"r",encoding="UTF-8") as pf:
        parser_output_lines=pf.readlines()
    parser_output_lines.pop()
    #we append the lines into a list thereby it is 2d list parser_output_list
    for line in parser_output_lines:
        parser_output_list.append(line.split())
    return parser_output_list
#===========================================================
parserOutputList=get_parser_output_list()
#===========================================================

def get_prune_output_list():
    #Open pruner file and store all its words into a 2d list
    prune_output_list=[]
    f=open(prune_file_input,"r",encoding="UTF-8")
    for line in f:
        prune_output_list.append(line.strip())
    f.close()
    return prune_output_list
#======================================================
pruneOutputList=get_prune_output_list()
#======================================================

def get_wx_output_list():
#open wx file and append it into a list
    wx_output_list=[]
    with open(wx_file_input,"r",encoding="UTF-8") as pf:
        wx_list=pf.readlines()
        wx_output_list=wx_list[0].split()
    return wx_output_list
#=======================================================
wxOutputList=get_wx_output_list()
#=======================================================

def get_root_word_dict(pruneOutputList):
    #root word dictionary
    root_word_dict={} #key=root_word and value is wx_word
    for sent in pruneOutputList:
        split_sent=sent.split("\t")
        wx_word=split_sent[1]
        root_word=split_sent[2]
        root_word_dict[root_word]=wx_word
    return root_word_dict
#========================================================
rootWordDict=get_root_word_dict(pruneOutputList)
#========================================================

def get_root_word_dict_reverse(pruneOutputList):
    root_word_dict_reverse={} #key==wx_word and value is root_word from prune output
    for sent in pruneOutputList:
        split_sent=sent.split("\t")
        wx_word=split_sent[1]
        root_word=split_sent[2]
        root_word_dict_reverse[wx_word]=root_word
    return root_word_dict_reverse
#============================================================
rootWordDictReverse=get_root_word_dict_reverse(pruneOutputList)
#=============================================================

def get_suffix_dictionary():
#creating a suffix dictionary where key is word and value is suffix a.k.a 8th vector
    suffix_dictionary={}
    word=str()
    for sent in pruneOutputList:
        split_sent=sent.split("\t")
        wx_word=split_sent[1]
        #print(split_sent)
        suffix=split_sent[6]
        suffix_dictionary[wx_word]=suffix
    return suffix_dictionary
#==============================================================
def get_person_dictionary():
#creating a suffix dictionary where key is word and value is suffix a.k.a 8th vector
    person_dictionary={}
    word=str()
    for sent in pruneOutputList:
        split_sent=sent.split("\t")
        wx_word=split_sent[1]
        #print(split_sent)
        person=split_sent[5]
        person_dictionary[wx_word]=person
    return person_dictionary
#==============================================================
suffixDictionary=get_suffix_dictionary()
#===============================================================

def get_wx_words_dictionary():
#Creating a dictionary for wx_words and their indexes
    wx_words_dictionary={} #wx_words are value and keys are indexes.
    index=1
    for words in wxOutputList:
        wx_words_dictionary[index]=words
        index+=1
    temp_wx_words_dict=wx_words_dictionary
    return wx_words_dictionary
#=================================================================
wxWordsDictionary=get_wx_words_dictionary()
#=================================================================

def get_parser_output_dict():
#creating a dictionary for parser_output_list
    parser_output_dict={}
    index=1
    for par_value in parserOutputList:
        parser_output_dict[index]=par_value
        index+=1
    return parser_output_dict
#===============================================================
parserOutputDict=get_parser_output_dict()
#================================================================

def get_wx_words_dictionary_new():
    #Creating a reverse dictionary for wx_words and their indexes
    wx_words_dictionary_new={} #wx_words are key and values are indexes.
    index=1
    for words in wxOutputList:
        wx_words_dictionary_new[words]=index
        index+=1
    temp_wx_words_dict=wx_words_dictionary_new
    return wx_words_dictionary_new
#==================================================================
wxWordsDictinaryNew=get_wx_words_dictionary_new()
#==================================================================

def get_NER_dict():
    #Open NER file and append its output into a list
    NER_dict={}
    inx=0
    y=open(ner_file_input,"r")
    for line in y:
        inx+=1
        token=line.strip()
        if token.split("\t")[1]!="O":
            wx_word=wxWordsDictionary[inx]
            #print(wx_word)
            NER_dict[wx_word]=token.split("\t")[1]
    return NER_dict
#====================================================================
nerDict=get_NER_dict()
#====================================================================

concept_list=[]
used_root_word=set()
updated_root_word={}
#====================================================================
def get_info_list_final(parserOutputList):
    info_list_final=[] #list containing important values from parser output file
    for line in parserOutputList:
        info_list_temp=[]
        word_index=int(line[0])
        pos_tag=line[3]
        class_index=line[6]
        word_info=line[7]
        info_list_temp.append(word_index)
        info_list_temp.append(pos_tag)
        info_list_temp.append(class_index)
        info_list_temp.append(word_info)
        info_list_final.append(info_list_temp)
    return info_list_final
#====================================================================
infoListFinal=get_info_list_final(parserOutputList)
#====================================================================

def get_TAM_dictionary_list():
    f=open("dictionaries/TAM-num-per-details.tsv.wx","r")
    TAM_dictionary_list=[]
    data=f.readlines()
    for line in data:
        line=line.split("\t")
        line=[s.strip() for s in line]
        TAM_dictionary_list.append(line)

    for line in TAM_dictionary_list:
        line.pop(0)
        return TAM_dictionary_list
#===================================================================
tamDictionaryList=get_TAM_dictionary_list()
#===================================================================

def search_concept(search_word):
    key=0
    for word in concept_dictionary_list:
        if word==search_word:
            key=1
            break
    if key==0:
        print("Warning:{} not found in dictionary.".format(search_word))    

#========================================================
def get_group_list(parserOutputList):
#To generate groups,"Not clear about it's output.please refer"
    group_list=[]
    index=len(parserOutputList)
    for val in range(index):
        if val==index-1 or parserOutputList[val][7]=="pof" or parserOutputList[val][7]=="pof__cn":
            group_list.append("0")
            #print(parser_output_list[val][1])
        elif parserOutputList[val][7]=="lwg__psp":
            group_list.append("-1")
            #print(parser_output_list[val][1])
        else:
            group_list.append("1")
    return group_list
#===========================================================
groupList=get_group_list(parserOutputList)
#===========================================================
#Row 2 of USR Which is Concept 
#for every element in wx_output_list,check its POS TAG
#the third column in parser_output_list[][3] is POS TAG,index from 0
already_visited={} #it is currently being used for VAUX and class words which have to be ignored while checking
VM_already_visited={} #To check if VM is already updated or not.Used only for verb groups.Key is wx_word and value is updated verbgroup

#=====================================================
def for_VM_no__1(row_2):
    for word in range(len(row_2)):
        if "+" in row_2[word]:
            ini_part=row_2[word].split("+",1)[0].strip("_1")
            
            final_part=row_2[word].split("+",1)[1]
            #print("finalpart:",final_part)
            row_2[word]=ini_part+"+"+final_part
    return row_2

#========================================================
def get_8th_vector(word, suffixDictionary):
    vector_8th=suffixDictionary[word]
    return vector_8th

#======================================================       
def get_root_word(word, rootWordDictReverse):#updated
    root_word=rootWordDictReverse[word]
    return root_word

#=================================================================   
def for_handling_nnc_tag_or_pof(word,class_index,wxWordsDictionary,word_info):
    # print("word  "+word)
    # print("class_index  "+str(class_index))
    # print(wxWordsDictionary)
    # print(infoListFinal)
    root_word=get_root_word(word, rootWordDictReverse)
    class_word=wxWordsDictionary[class_index]
    already_visited[class_index]=class_word
    first_key=class_index
    if len(already_visited)>1:
        first_key = next(iter(already_visited))
        del already_visited[first_key] 
    # print(root_word)
    # print("already")
    # print(already_visited)
    # print("VM")
    # print(VM_already_visited)
    if class_word in VM_already_visited and class_index == first_key:
        root_word_class=VM_already_visited[class_word]
    else:   
        root_word_class=get_root_word(class_word, rootWordDictReverse)
    if(root_word_class.rfind('+')==-1):
        root_word_class+="_1"
    else:
        last_plus_index = root_word_class.rfind('+')
        root_word=root_word_class[:last_plus_index]+"+"+root_word
        root_word_class=root_word_class[last_plus_index + 1:]
    # print(word_info)
    if word_info.strip()=="pof__cn":
        # print('true')
        final_word=root_word+"_1"+"+"+root_word_class
        VM_already_visited[class_word]=final_word
    if word_info=="pof":
        final_word=root_word+"+"+root_word_class
        VM_already_visited[class_word]=final_word
    # print(final_word)
    return final_word

#=============================================================
#Step 1:Take the second row and identfify TAMs present in them.
def identify_vb(concept_list):
    tam_list_row2=[]
    # print(concept_list)
    for concept in concept_list:
        if "-" in concept:
            tam_list_row2.append(concept)
    return tam_list_row2
  