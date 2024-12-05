import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH


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


def add_space_around_punctuation(sentence):
    # Define punctuation to add spaces around
    punctuations = [",", "#", "(", ")", ":", ";", "-", "%", "'", '"', "’", "‘", "*", "&", "@", "!", "/", "$", "^", "=", "।", "|", ".", "?"]
    within_angle_brackets = False

    result = ""
    for char in sentence:
        if char == "<":
            within_angle_brackets = True
        elif char == ">":
            within_angle_brackets = False

        if not within_angle_brackets and char in punctuations:
            char = f" {char} "

        result += char

    # Ensure there are no multiple spaces
    result = " ".join(result.split())
    return result


def remove_starting_connectives(sentence):
    SIMPLE_CONNECTIVES = ['और', 'तभी', 'एवं', 'इसलिए', 'इसलिये', 'क्योंकि', 'जबकि', 'तथा', 'ताकि', 'मगर', 'लेकिन', 'किंतु', 'परंतु', 'फिर भी', 'या', 'तथापि',
                          'नहीं तो', 'व', 'चूंकि', 'चूँकि', 'वरना', 'अन्यथा', 'बशर्तें', 'हालाँकि', 'इसीलिये', 'इसीलिए', 'इसलिए', 'अथवा', 'अतः', 'अर्थात्', 'जब', 'तो', 'परन्तु', 'कि', 'बल्कि', 'पर']
    
    # Loop through the connectives
    for conn in SIMPLE_CONNECTIVES:
        # If the sentence starts with a connective, remove it
        if sentence.startswith(conn + " "):
            sentence = sentence[len(conn):].strip()
            break
    return sentence


if __name__ == "__main__":
    file_name_input = f"{PATH}txt_files/bh-1"
    file_name_output = f"{PATH}txt_files/bh-1"
    
    with open(file_name_input, "r", encoding="UTF-8") as f:
        sentence = f.readline().strip()
        sentence = add_space_around_punctuation(sentence)
        sentence = check_punctuation(sentence)
        sentence = remove_starting_connectives(sentence)

    os.remove(file_name_input)
    with open(file_name_output, "w", encoding="UTF-8") as f:
        f.write(sentence)
