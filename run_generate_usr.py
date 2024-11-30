# import os
# file_name=open("sentences_for_USR","r",encoding="UTF-8")
# file_to_paste=open("txt_files/bh-1","r+",encoding="UTF-8")
# file_to_paste_temp=open("bh-2","r+",encoding="UTF-8") #creating a temporary file,just to keep record of the original sentence
# for sentence in file_name:
#     sentence=sentence.strip()
#     print(sentence)
#     try:
#         file_to_paste=open("txt_files/bh-1","r+",encoding="UTF-8")
#         s_id=sentence.split("  ")[0]
#         #print(s_id)
#         orig_sent=sentence.split("  ")[1].strip()
#         orig_sent_copy=sentence.split("  ")[1]
#         file_to_paste.seek(0)
#         file_to_paste.write(orig_sent)
#         file_to_paste.truncate()
#         file_to_paste.close()
#         #print("bh-1 closed")
#         #------------------------------------------------------
#         #Creating a temporary file for keeping record of the original sentence
#         file_to_paste_temp.seek(0)
#         file_to_paste_temp.write(orig_sent)
#         file_to_paste_temp.truncate()
#         #file_to_paste_temp.close()
#         #print("bh-2 created")
#         #----------------------------------------------------------
#         # os.system("python3 sentence_check.py")
#         os.system("python3 run_script.py")
#         os.system("python3 complete_usr.py>bulk_USRs/"+s_id)
#         # os.system("python3 generate_usr.py>bulk_USRs/"+s_id)
#     except Exception as e:
#         print(e)

# # After processing all sentences, truncate the "sentences_for_USR" file
# file_name.close()


import os
import subprocess

# Open the files
file_name = open("txt_files/sentences_for_USR", "r", encoding="UTF-8")
file_to_paste = open("txt_files/bh-1", "r+", encoding="UTF-8")
file_to_paste_temp = open("txt_files/bh-2", "r+", encoding="UTF-8")  # Temporary file to keep a record of the original sentence

# Open a log file for writing timeout and error messages
with open("timeout_log.txt", "a", encoding="UTF-8") as log_file:
    for sentence in file_name:
        sentence = sentence.strip()
        print(sentence)  # Print the sentence being processed

        try:
            # Open the file to paste
            file_to_paste = open("txt_files/bh-1", "r+", encoding="UTF-8")
            s_id = sentence.split("  ")[0]
            orig_sent = sentence.split("  ")[1].strip()

            # Write the original sentence to bh-1
            file_to_paste.seek(0)
            file_to_paste.write(orig_sent)
            file_to_paste.truncate()
            file_to_paste.close()

            # Create a temporary file to keep a record of the original sentence
            file_to_paste_temp.seek(0)
            file_to_paste_temp.write(orig_sent)
            file_to_paste_temp.truncate()

            # Run scripts with a timeout of 120 seconds (2 minutes)
            try:
                subprocess.run(["python3", "intermediate_scripts/run_script.py"], timeout=120)
                subprocess.run(["python3", "modules/complete_usr.py"], stdout=open(f"txt_files/bulk_USRs/{s_id}", "w"), timeout=120)
            except subprocess.TimeoutExpired:
                log_file.write(f"{s_id}\t{orig_sent} ------>timed out\n")
                continue  # Skip to the next sentence if the timeout occurs

        except Exception as e:
            log_file.write(f"{s_id}{orig_sent}'------>error occur\n")
            continue  # Move to the next sentence if an error occurs

# Close the files
file_name.close()
file_to_paste_temp.close()
