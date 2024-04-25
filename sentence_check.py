import os

def check_punctuation(sentence):
    flag = 0
    list_punc_with_space = [" |", " ?", " !", " ।", " ."]
    list_punc_without_space = ["|", "?", "!", "।"]

    if sentence.endswith(tuple(list_punc_with_space)):
        flag = 1
        last_word = sentence[-1]
        if last_word == "।" or last_word == "|":
            sentence = sentence.replace(last_word, ".")
    elif sentence.endswith(tuple(list_punc_without_space)):
        flag = 1
        last_word = sentence[-1]
        if last_word == "।" or last_word == "|":
            sentence = sentence.replace(last_word, " " + ".")
        else:
            sentence = sentence.replace(last_word, " " + last_word)
    elif sentence.endswith(tuple(".")):
        flag = 1
        sentence = sentence.replace(".", " " + ".")
    elif sentence.endswith(tuple(" .")):
        flag = 1
        sentence = sentence.replace(".", ".")

    if flag == 0:
        sentence += "."

    return sentence

def remove_allpunc(sentence):
    punctuations = [",", "#", "<", ">", "(", ")", ":", ";", "-", "%", "'", '"', "’", "‘", "*", "&", "@"]
    for sym in punctuations:
        if sym in sentence:
            sentence = sentence.replace(sym, " ")
    return sentence

def remove_starting_connectives(sentence):
    SIMPLE_CONNECTIVES = ['और', 'एवं', 'इसलिए', 'क्योंकि', 'जबकि', 'तथा', 'ताकि', 'मगर', 'लेकिन', 'किंतु', 'परंतु', 'फिर भी', 'या', 'तथापि',
                      'नहीं तो', 'व', 'चूंकि', 'चूँकि', 'वरना', 'अन्यथा', 'बशर्तें', 'हालाँकि', 'इसीलिये', 'इसीलिए' , 'इसलिए', 'अथवा', 'अतः', 'अर्थात्', 'जब', 'तो', 'परन्तु', 'कि', 'बल्कि', 'पर']
    first_word = sentence.split()[0]
    if first_word in SIMPLE_CONNECTIVES:
        sentence = " ".join(sentence.split()[1:])
    return sentence

if __name__ == "__main__":
    file_name_input = "txt_files/bh-1"
    file_name_output = "txt_files/bh-1"
    
    with open(file_name_input, "r", encoding="UTF-8") as f:
        sentence = f.readline().strip()
        sentence = remove_allpunc(sentence)
        sentence = check_punctuation(sentence)
        sentence = remove_starting_connectives(sentence)

    os.remove(file_name_input)
    with open(file_name_output, "w", encoding="UTF-8") as f:
        f.write(sentence)
