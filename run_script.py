# import os

# os.system("python3 sentence_check.py")
# # os.system("isc-parser -i txt_files/bh-1 > txt_files/parser-output.txt")
# os.system("python3 dependency.py") 
# os.system("utf8_wx txt_files/bh-1 > txt_files/wx.txt")
# os.system("python3 morph_call-1.py")
# os.system("python3 converter.py")
# os.system("python3 ner_call.py ")
# # os.system("python3 generate_usr.py") 


import os
import time


start_time = time.time()
os.system("python3 sentence_check.py")
print("Time taken for sentence_check.py:", time.time() - start_time)

start_time = time.time()
os.system("python3 dependency.py")
print("Time taken for dependency.py:", time.time() - start_time)

start_time = time.time()
os.system("utf8_wx txt_files/bh-1 > txt_files/wx.txt")
print("Time taken for utf8_wx:", time.time() - start_time)

start_time = time.time()
os.system("python3 morph_call-1.py")
print("Time taken for morph_call-1.py:", time.time() - start_time)

start_time = time.time()
os.system("python3 converter.py")
print("Time taken for converter.py:", time.time() - start_time)

start_time = time.time()
os.system("python3 ner_call.py")
print("Time taken for ner_call.py:", time.time() - start_time)

print("------------------------------")
# os.system("python3 generate_usr.py")
# print("Time taken for generate_usr.py:", time.time() - start_time)
