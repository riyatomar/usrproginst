import sys, os, re
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH

def modify_digits_in_text(text):
    # Use a regular expression to find all sequences of digits with commas or points in the text
    modified_text = re.sub(r'\b(\d{1,3}(,\d{2})+(,\d{3})*(\.\d+)?|\d{1,3}(,\d{3})*(\.\d+)?)\b', r'<\1>', text)

    # Find all occurrences of text within < and > and remove commas within them
    modified_text = re.sub(r'<([^<>]+)>', lambda match: f"<{match.group(1).replace(',', '')}>", modified_text)

    # Combine adjacent words within < and >
    modified_text = re.sub(r'(<[^<>]+>)\s*(<[^<>]+>)', r'\1\2', modified_text)

    return modified_text


def process_and_save_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # Read the content of the input file
            text = input_file.read()

            # Modify the text
            modified_text = modify_digits_in_text(text)

            # Write the modified text to the output file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(modified_text)

    except FileNotFoundError:
        print(f"File not found: {input_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
input_file_path_example = f"{PATH}txt_files/bh-1"
output_file_path_example = f"{PATH}txt_files/bh-1"

process_and_save_file(input_file_path_example, output_file_path_example)

