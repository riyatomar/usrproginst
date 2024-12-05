import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH

def process_text_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # List to store processed lines
        processed_lines = []

        # Process each line
        for line in lines:
            # Check if the line contains '*conj' or '*disjunct'
            if '*conj' in line or '*disjunct' in line:
                continue  # Skip this line

            # Remove '.txt' from the line
            processed_line = line.replace('.txt', '')

            # Append the processed line to the list
            processed_lines.append(processed_line)
        
        # Write the processed lines to the output file
        with open(output_file, 'w') as file:
            file.writelines(processed_lines)

        # print(f"Processing complete. Output written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input and output file names
input_filename = f'{PATH}usr_processed/usr_file.txt'  # Replace with your input file name
output_filename = f'{PATH}txt_files/final_usr_file.txt'  # Replace with your desired output file name

# Call the function to process the file
process_text_file(input_filename, output_filename)
