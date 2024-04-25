import os
import re 

def create_pos_mapped_dict(pos_tag):
    mapper_dict={"NN":"n","NST":"nst","NNP":"n","NEG":"avy","PRP":"p",
                "PSP":"prsg","DEM":"p","VM":"v","VAUX":"v","JJ":"adj",
                "RB":"adv","RP":"avy","CC":"avy","CL":"avy","WQ":"p",
                "QF":"avy","QC":"num","QO":"num","INTF":"avy","INJ":"avy",
                "UT":"avy","UNK":"unk","SYM":"s","XC":"c","NNPC":"n"}
    for inx in range(len(pos_tag)):
        if pos_tag[inx] in mapper_dict:
            mapped_op=mapper_dict[pos_tag[inx]]
            pos_tag[inx]=mapped_op
    return pos_tag

def process_morph_output(pos_tag, morph_file):
    words_to_ignore_for_root = ["hE"]
    f = open(morph_file, "r")
    item_c = 0
    counter = 1
    word_counter = 0
    filtered_match = []
    final_match = []
    for line in f:
        matched_span = []
        flag = 0
        matches = re.findall("<cat:([^>]*)", line.strip())
        if len(matches) == 0:
            input_str = line
            start_marker = "^"
            end_marker = "/"
            start_index = input_str.find(start_marker)
            end_index = input_str.find(end_marker, start_index)
            root_word_value = input_str[start_index+1:end_index]
            matched_span.append("/" + root_word_value + "<cat:unk><case:unk><gen:unk><num:unk><per:unk><tam:unk>")
            filtered_match.append(matched_span)
            continue
        for word_inx in range(len(matches)):
            if matches[word_inx] == pos_tag[counter]:
                first_inx = word_inx
                sent = line.split("/")[first_inx+1]
                matched_span.append("/" + sent.strip())
                flag = 1
        if flag == 0:
            first_inx = 0
            sent = line.split("/")[first_inx+1]
            matched_span.append("/" + sent.strip())
        counter += 1
        filtered_match.append(matched_span)
    f.close()
    original_word = []
    f = open(morph_file, "r")
    for sent in f:
        input_str = sent
        start_marker = "^"
        end_marker = "/"
        start_index = input_str.find(start_marker)
        end_index = input_str.find(end_marker, start_index)
        original_word.append(input_str[start_index+1:end_index])
    original_word.pop()
    for span_inx in range(len(filtered_match)-1):
        flag = 0
        matched_span = filtered_match[span_inx]
        for matches in matched_span:
            input_str = matches
            start_marker = "/"
            end_marker = "<"
            if "<" not in input_str:
                end_marker = "$"
            start_index = input_str.find(start_marker)
            end_index = input_str.find(end_marker, start_index)
            root_word_value = input_str[start_index+1:end_index]
            if root_word_value in words_to_ignore_for_root:
                break
            if root_word_value != original_word[span_inx]:
                flag = 1
                final_match.append(matches)
                break
        if flag == 0:
            final_match.append(matched_span[0])
    return final_match, original_word

def extract_root_words(final_span):
    root_word = []
    for span in final_span:
        input_str = span
        start_marker = "/"
        end_marker = "<"
        if "<" not in input_str:
            end_marker = "$"
        start_index = input_str.find(start_marker)
        end_index = input_str.find(end_marker, start_index)
        root_word_value = input_str[start_index+1:end_index]
        root_word.append(root_word_value)
    return root_word

def extract_gnp_and_tam(matched_span):
    gender = []
    number = []
    person = []
    tam = []
    for sent in matched_span:
        input_str = sent
        start_marker = "<gen:"
        end_marker = ">"
        start_index = input_str.find(start_marker)
        end_index = input_str.find(end_marker, start_index)
        if start_index != -1:
            gender.append(input_str[start_index+1:end_index])
        else:
            gender.append("gen:unk")
        
        start_marker = "<num:"
        end_marker = ">"
        start_index = input_str.find(start_marker)
        end_index = input_str.find(end_marker, start_index)
        if start_index != -1:
            number.append(input_str[start_index+1:end_index])
        else:
            number.append("num:unk")
        
        start_marker = "<per:"
        end_marker = ">"
        start_index = input_str.find(start_marker)
        end_index = input_str.find(end_marker, start_index)
        if start_index != -1:
            person.append(input_str[start_index+1:end_index])
        else:
            person.append("per:unk")

        start_marker = "<tam:"
        end_marker = ">"
        start_index = input_str.find(start_marker)
        end_index = input_str.find(end_marker, start_index)
        if start_index != -1:
            tam.append(input_str[start_index+1:end_index])
        else:
            tam.append("tam:unk")
    return gender, number, person, tam

def write_final_output(original_word, root_word, gender, number, person, tam, prune_file):
    f = open(prune_file, "w")
    for i in range(len(original_word)):
        try:
            f.write(str(i+1) + "\t" + original_word[i] + "\t" + root_word[i].strip("*") + "\t" + gender[i].split(":")[1] + "\t" + number[i].split(":")[1] + "\t" + person[i].split(":")[1] + "\t" + tam[i].split(":")[1] + "\n")
        except:
            f.write(str(i+1) + "\t" + original_word[i] + "\t" + root_word[i].strip("*") + "\t" + "unk" + "\t" + "unk" + "\t" + "unk" + "\t" + "unk" + "\n")

if __name__ == "__main__":
    input_folder = "txt_files/"
    sentence_file = "wx.txt"
    single_concept_inp = "concept.txt"
    single_concept_out = "concept.txt-out.txt"
    output_file = "morph-output.txt"

    input_file_path = os.path.join(input_folder, sentence_file)
    output_file_path = os.path.join(input_folder, output_file)

    with open(output_file_path, "w") as out:
        out.write("")

    if os.path.isfile(input_file_path):
        with open(input_file_path, "r") as inp:
            sentence = inp.read().strip()
            words = sentence.split()

            for word in words:
                if word.startswith("<") and word.endswith(">"):
                    with open(output_file_path, "a") as out:
                        out.write(word + "\n")
                else:
                    with open(single_concept_inp, "w") as sc:
                        sc.write(word)

                    os.system("sh run_morph-analyser.sh " + single_concept_inp)

                    with open(single_concept_out, "r") as con_out:
                        output = con_out.read().strip()

                    with open(output_file_path, "a") as out:
                        out.write(output + "\n")

                    with open(single_concept_inp, "w") as sc:
                        sc.write("")

                    with open(single_concept_out, "w") as con_out:
                        con_out.write("")

        parser_file = "txt_files/parser-output.txt"
        prune_file = "txt_files/prune-output.txt"
        morph_file = "txt_files/morph-output.txt"

        f = open(parser_file)
        pos_tag = []
        matched_span = []
        flag = 0
        for line in f:
            try:
                cat = line.split("\t")[3].strip()
                pos_tag.append(cat)
            except:
                pass
        f.close()

        pos_tag = create_pos_mapped_dict(pos_tag)
        matched_span, original_word = process_morph_output(pos_tag, morph_file)
        root_word = extract_root_words(matched_span)
        gender, number, person, tam = extract_gnp_and_tam(matched_span)
        write_final_output(original_word, root_word, gender, number, person, tam, prune_file)
