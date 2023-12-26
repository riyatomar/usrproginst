import os
import subprocess

file_name = open("sentences_for_USR", "r", encoding="UTF-8")
bulk_folder = "bulk_sent_type"
if not os.path.exists(bulk_folder):
    os.makedirs(bulk_folder)

file_to_paste_temp = open("bh-2", "r+", encoding="UTF-8")

combine_concepts=[]

for sentence in file_name:
    sentence = sentence.strip()
    try:
        file_to_paste = open("txt_files/bh-1", "r+", encoding="UTF-8")
        s_id = sentence.split("  ")[0]
        orig_sent = sentence.split("  ")[1].strip()
        orig_sent_copy = sentence.split("  ")[1]
        store=""
        if s_id[len(s_id)-1] == 'F':
            store="fragment"
        elif s_id[len(s_id)-1] == 'T':
            store="title"
        elif s_id[len(s_id)-1] == 'H':
            store="heading"
        else:
            if "nahI" in orig_sent or "nahIM" in orig_sent:
                store="negative"
            else:
                if "?" in orig_sent:
                    store="interrogative"
                elif "|" in orig_sent or "." in orig_sent:
                    store="affirmative"
                elif "!" in orig_sent:
                    store="exclamatory"

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

        with open(os.path.join(bulk_folder, s_id), 'w') as uif:
            temp_store=""
            store_indexes = subprocess.check_output(["/usr/bin/python3", "indexing_module.py"], text=True)
            for i in range(int(store_indexes.rstrip("\n")[-1])-1):
                temp_store+=store+","
            temp_store+=store
            uif.write(temp_store)
            combine_concepts.clear()
        
        
    
        

    except Exception as e:
        print(e)
    
    


file_to_paste_temp.close()
