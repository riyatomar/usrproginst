import os

file_name = open("sentences_for_USR", "r", encoding="UTF-8")
bulk_index_folder = "bulk_index"
if not os.path.exists(bulk_index_folder):
    os.makedirs(bulk_index_folder)

file_to_paste_temp = open("bh-2", "r+", encoding="UTF-8")

for sentence in file_name:
    sentence = sentence.strip()
    print(sentence)
    try:
        file_to_paste = open("txt_files/bh-1", "r+", encoding="UTF-8")
        s_id = sentence.split("  ")[0]
        orig_sent = sentence.split("  ")[1].strip()
        orig_sent_copy = sentence.split("  ")[1]

        # Write original sentence to 'bh-1' file
        file_to_paste.seek(0)
        file_to_paste.write(orig_sent)
        file_to_paste.truncate()
        file_to_paste.close()

        # Write original sentence to temporary file 'bh-2'
        file_to_paste_temp.seek(0)
        file_to_paste_temp.write(orig_sent)
        file_to_paste_temp.truncate()

        # Execute commands
        os.system("python3 run_script.py")
        os.system("python3 sem_cat_module.py > {}/{}".format(bulk_index_folder, s_id))

    except Exception as e:
        print(e)

file_to_paste_temp.close()
