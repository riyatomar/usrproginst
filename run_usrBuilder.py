import os

# List of commands to execute
commands = [
    "python3 run_generate_usr.py",
    "python3 intermediate_scripts/run_usr.py",
    "python3 process_usr_files/csv2vertical_format.py txt_files/bulk_USRs_mod/ usr_processed/verticle_USRs",
    "python3 process_usr_files/merger.py usr_processed/verticle_USRs/ usr_processed/merged_USR",
    "python3 process_usr_files/add_sent_id.py usr_processed/merged_USR usr_processed/tagged_USRs",
    "python3 process_usr_files/vertical_usr_segregator.py usr_processed/tagged_USRs usr_processed/vertical_segregated",
    "python3 complete_cnx.py",
    "python3 process_usr_files/merge_without_id.py usr_processed/final_outputs usr_processed/usr_file.txt",
    "python3 process_usr_files/remove_txt.py",
    "python3 process_usr_files/remove_intermediate_files.py"
]

# Execute commands
for command in commands:
    print(f"Executing: {command}")
    exit_code = os.system(command)
    if exit_code != 0:
        print(f"Command failed with exit code {exit_code}: {command}")
        break  # Stop execution if a command fails
