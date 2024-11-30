# Function to read a file and return its lines as a list
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Function to write aligned content with unique IDs to an output file
def write_aligned_file_with_ids(output_path, aligned_data):
    with open(output_path, 'w', encoding='utf-8') as file:
        # for idx, (en, hi) in enumerate(aligned_data, start=1):
        for en, hi in aligned_data:
            file.write(f"{en.strip()}\t{hi.strip()}\n\n")


# Main function to align text from two files and assign unique IDs
def align_text_with_ids(english_file, hindi_file, output_file):
    english_lines = read_file(english_file)
    hindi_lines = read_file(hindi_file)

    # Ensure both files have the same number of lines
    if len(english_lines) != len(hindi_lines):
        print("Warning: The number of lines in the files do not match.")
        return

    # Pair English and Hindi lines together
    aligned_content = zip(english_lines, hindi_lines)

    # Write the aligned content with IDs to the output file
    write_aligned_file_with_ids(output_file, aligned_content)

    print(f"Aligned text with IDs has been written to {output_file}")

# Specify file paths
english_file_path = 'train.en'  # Path to English text file
hindi_file_path = 'train.hi'    # Path to Hindi text file
output_file_path = 'aligned_en_hi.txt'  # Path to output file

# Run the alignment
align_text_with_ids(english_file_path, hindi_file_path, output_file_path)
