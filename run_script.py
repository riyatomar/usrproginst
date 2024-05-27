import os


os.system("python3 digit_identifier.py") 
os.system("python3 sentence_check.py")
os.system("python3 remove_space.py")
os.system("utf8_wx txt_files/bh-1 > txt_files/wx.txt")

file_name_input = "txt_files/bh-1"
with open(file_name_input, "r", encoding="UTF-8") as f:
    content = f.read()
content = content.replace("<", "").replace(">", "")
with open(file_name_input, "w", encoding="UTF-8") as f:
    f.write(content)

os.system("python3 dependency.py") 
os.system("python3 ner_call.py")
# os.system("python3 prune_out_generator.py")
os.system("python3 morph_call-1.py")
os.system("python3 converter.py")