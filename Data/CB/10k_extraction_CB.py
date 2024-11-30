# # Function to read and split the input text file
# def read_text_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     # Split each line into English and Hindi parts
#     data = []
#     for line in lines:
#         parts = line.strip().split('\t')
#         if len(parts) == 2:  # Ensure the line has both English and Hindi
#             data.append((parts[0], parts[1]))
#     return data

# # Function to filter and add unique IDs to sentence pairs
# def process_and_add_ids(data, min_tokens, max_sentences, output_file):
#     unique_english_texts = set()
#     processed_sentences = []

#     for en_text, hi_text in data:
#         # Tokenize English text and check token count
#         if len(en_text.split()) > min_tokens and en_text not in unique_english_texts:
#             processed_sentences.append((len(processed_sentences) + 1, en_text, hi_text))
#             unique_english_texts.add(en_text)

#             # Stop if we reach the maximum desired sentences
#             if len(processed_sentences) == max_sentences:
#                 break

#     # Write processed sentences with IDs to the output file
#     with open(output_file, 'w', encoding='utf-8') as file:
#         for id, en_text, hi_text in processed_sentences:
#             file.write(f"{id}\t{en_text}\t{hi_text}\n")

#     print(f"Processed and added IDs to {len(processed_sentences)} sentences in {output_file}")

# # Main function
# def main():
#     input_file = 'aligned_en_hi.txt'  
#     output_file = '10k_CB_hi_en_dataset.txt'
#     min_tokens = 12  
#     max_sentences = 10000 

#     # Read the input data
#     text_data = read_text_file(input_file)

#     # Process the text and add unique IDs
#     process_and_add_ids(text_data, min_tokens, max_sentences, output_file)

# # Run the script
# if __name__ == "__main__":
#     main()


import re  # Import regex module for advanced filtering

# Function to read and split the input text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # Extract English and Hindi parts from the 4th and 5th columns
    data = []
    for line in lines:
        parts = line.strip().split('\t')  # Split by tab
        if len(parts) >= 5:  # Ensure line has at least 5 columns
            en_text = parts[3]  # 4th column: English
            hi_text = parts[4]  # 5th column: Hindi
            data.append((en_text, hi_text))
    return data

# Function to filter Hindi text and add unique IDs
def process_and_add_ids(data, min_tokens, max_sentences, output_file):
    unique_english_texts = set()
    processed_sentences = []

    # Regex pattern to check punctuation in the middle
    punctuation_pattern = re.compile(r'.*[?.!।].+')

    for en_text, hi_text in data:
        # Skip Hindi text with punctuation in the middle
        if punctuation_pattern.match(hi_text):
            continue

        # Tokenize English text and check token count
        if len(en_text.split()) > min_tokens and en_text not in unique_english_texts:
            processed_sentences.append((len(processed_sentences) + 1, en_text, hi_text))
            unique_english_texts.add(en_text)

            # Stop if we reach the maximum desired sentences
            if len(processed_sentences) == max_sentences:
                break

    # Write processed sentences with IDs to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for id, en_text, hi_text in processed_sentences:
            file.write(f"{id}\t{en_text}\t{hi_text}\n")

    print(f"Processed and added IDs to {len(processed_sentences)} sentences in {output_file}")

# Main function
def main():
    input_file = '/home/lc4eu/LC/Data/CB/hindencorp05.plaintext'  # Input file path
    output_file = '10k_CB_hi_en_dataset.txt'  # Output file path
    min_tokens = 12  # Minimum tokens in English sentence
    max_sentences = 10000  # Maximum number of sentences to process

    # Read the input data
    text_data = read_text_file(input_file)

    # Process the text and add unique IDs
    process_and_add_ids(text_data, min_tokens, max_sentences, output_file)

# Run the script
if __name__ == "__main__":
    main()
