import os
os.system("python3 sentence_check.py")
# os.system("isc-parser -i txt_files/bh-1 > txt_files/parser-output.txt")
os.system("python3 dependency.py") 
os.system("utf8_wx txt_files/bh-1 > txt_files/wx.txt")
os.system("python3 morph_call-1.py")
os.system("python3 converter.py")
# os.system("python3 ner_call.py ")
# os.system("python3 generate_usr.py") 
