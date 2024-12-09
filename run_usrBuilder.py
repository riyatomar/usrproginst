import os
from modules.set_path import PATH

commands = [
    # f"python3 {PATH}run_generate_usr.py",
    f"python3 {PATH}intermediate_scripts/run_usr.py",
    f"python3 {PATH}process_usr_files/csv2vertical_format.py {PATH}txt_files/bulk_USRs_mod/ {PATH}usr_processed/verticle_USRs",
    f"python3 {PATH}process_usr_files/merger.py {PATH}usr_processed/verticle_USRs/ {PATH}usr_processed/merged_USR",
    f"python3 {PATH}process_usr_files/add_sent_id.py {PATH}usr_processed/merged_USR {PATH}usr_processed/tagged_USRs",
    f"python3 {PATH}process_usr_files/vertical_usr_segregator.py {PATH}usr_processed/tagged_USRs {PATH}usr_processed/vertical_segregated",
    f"python3 {PATH}cnx_module/complete_cnx.py",
    f"python3 {PATH}process_usr_files/merge_without_id.py {PATH}usr_processed/final_outputs {PATH}usr_processed/usr_file.txt",
    f"python3 {PATH}process_usr_files/remove_txt.py",
    f"python3 {PATH}process_usr_files/remove_intermediate_files.py"
]

# Execute commands
for command in commands:
    print(f"Executing: {command}")
    exit_code = os.system(command)
    if exit_code != 0:
        print(f"Command failed with exit code {exit_code}: {command}")
        break  # Stop execution if a command fails
