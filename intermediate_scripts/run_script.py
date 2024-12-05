import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH

os.system(f"python3 {PATH}intermediate_scripts/digit_identifier.py") 
os.system(f"python3 {PATH}intermediate_scripts/sentence_check.py")
os.system(f"python3 {PATH}intermediate_scripts/remove_space.py")
os.system(f"utf8_wx {PATH}txt_files/bh-1 > {PATH}txt_files/wx.txt")

file_name_input = f"{PATH}txt_files/bh-1"
with open(file_name_input, "r", encoding="UTF-8") as f:
    content = f.read()
content = content.replace("<", "").replace(">", "")
with open(file_name_input, "w", encoding="UTF-8") as f:
    f.write(content)

os.system(f"python3 {PATH}intermediate_scripts/dependency_mapper.py") 
os.system(f"python3 {PATH}intermediate_scripts/ner_call.py")
# os.system(f"python3 {PATH}intermediate_scripts/prune_out_generator.py")
os.system(f"python3 {PATH}intermediate_scripts/morph_call-1.py")
os.system(f"python3 {PATH}intermediate_scripts/converter.py")
os.system(f"utf8_wx {PATH}txt_files/bh-1 > {PATH}txt_files/wx.txt")