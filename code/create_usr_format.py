
from wxconv import WXC

def devanagari_to_wx(word):
    wxc = WXC()
    wx_text = wxc.convert(word)
    return wx_text

def process_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        
        for line in lines:
            line = line.strip()  # Remove extra spaces or newline characters

            # Split the line into sentence id and sentence
            if '  ' in line:
                sentence_id, sentence = line.split('  ', 1)

                # Write the sentence ID part
                outfile.write(f"<sent_id= {sentence_id}>\n")

                # Write the sentence as a comment
                outfile.write(f"#{sentence}\n")

                # Split the sentence into words and process them
                words = sentence.strip().split()  # Split the sentence into words
                for word in words:
                    # Write each word in the specified format
                    outfile.write(f"{devanagari_to_wx(word)}_1\t-\t-\t-\t-\t-\t-\t-\t-\n")

                # Add %affirmative and close the sentence block
                outfile.write("%affirmative\n")
                outfile.write("</sent_id>\n\n\n\n")

# Example usage:
input_file = "not_gen.txt"  # Path to the file containing the original text
output_file = "gen_usr_format.txt"  # Path where the formatted text will be saved
process_text(input_file, output_file)

print("Text processing complete.")
