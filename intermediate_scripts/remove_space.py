import re

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
file_path = 'txt_files/bh-1'

# Call the function to remove extra spaces
remove_extra_spaces(file_path)

