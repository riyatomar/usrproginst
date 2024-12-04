import os

path = '/home/riya/usrproginst/'
commands = [
    f"python3 {path}run_generate_usr.py",
    f"python3 {path}intermediate_scripts/run_usr.py",
    f"python3 {path}process_usr_files/csv2vertical_format.py {path}txt_files/bulk_USRs_mod/ {path}usr_processed/verticle_USRs",
    f"python3 {path}process_usr_files/merger.py {path}usr_processed/verticle_USRs/ {path}usr_processed/merged_USR",
    f"python3 {path}process_usr_files/add_sent_id.py {path}usr_processed/merged_USR {path}usr_processed/tagged_USRs",
    f"python3 {path}process_usr_files/vertical_usr_segregator.py {path}usr_processed/tagged_USRs {path}usr_processed/vertical_segregated",
    f"python3 {path}complete_cnx.py",
    f"python3 {path}process_usr_files/merge_without_id.py {path}usr_processed/final_outputs {path}usr_processed/usr_file.txt",
    f"python3 {path}process_usr_files/remove_txt.py",
    f"python3 {path}process_usr_files/remove_intermediate_files.py"
]

# Execute commands
for command in commands:
    print(f"Executing: {command}")
    exit_code = os.system(command)
    if exit_code != 0:
        print(f"Command failed with exit code {exit_code}: {command}")
        break  # Stop execution if a command fails
