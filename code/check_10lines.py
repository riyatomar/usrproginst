import os

# Function to check if a file has exactly 10 lines
def check_file_lines(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file (and not a directory)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                # Count the number of lines
                line_count = sum(1 for _ in file)
                
                # Print the filename if it has exactly 10 lines
                if line_count == 11:
                    print(f"File: {filename} has 10 lines.")
                    
# Specify the directory containing the files
directory_path = 'bulk_USRs/'

# Run the function
check_file_lines(directory_path)

