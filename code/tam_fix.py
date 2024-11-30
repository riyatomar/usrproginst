import sys
import os

input_usr_folder = "bulk_USRs_mod1/"

usr_files = os.listdir(input_usr_folder)

def read_concept_row(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_line = lines[1].strip()
                return second_line, lines
            else:
                return None, None
    except Exception as e:
        return None, None
print("=====================================")
for file_name in usr_files:
    file_path = os.path.join(input_usr_folder, file_name)

    if os.path.isfile(file_path):
        second_line, file_lines = read_concept_row(file_path)
        if second_line is not None:
            hyphen_count = second_line.count("-")

            if hyphen_count > 1:
                hyphen_parts = second_line.split("-")
                corrected_line = hyphen_parts[0] + "-" + hyphen_parts[1]
                file_lines[1] = corrected_line + "\n"

                # Write the corrected lines back to the file
                with open(file_path, "w") as file:
                    file.writelines(file_lines)
                
                print(f"Corrected Second Line in {file_name} \n")
            else:
                print(f"No correction needed for Second Line in {file_name} \n")

print("=============================================")
