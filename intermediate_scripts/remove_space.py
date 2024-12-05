import sys, os, re
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH

def remove_extra_spaces(file_path):
    # Read text from the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove extra spaces using regular expressions
    modified_text = re.sub(r'\s+', ' ', text)

    # Write modified text back to the file
    with open(file_path, 'w') as file:
        file.write(modified_text)

# Provide the file path here
file_path = f'{PATH}txt_files/bh-1'

# Call the function to remove extra spaces
remove_extra_spaces(file_path)

