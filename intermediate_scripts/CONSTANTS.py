import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH

INPUT_FILE = f"{PATH}txt_files/bh-1"
INTERMEDIATE_PARSER_INPUT = f"{PATH}txt_files/inter_parser_input.txt"
INTERMEDIATE_PARSER_OUTPUT = f"{PATH}txt_files/inter_parser_output.txt"
CONSOLIDATED_PARSER_OUTPUT = f"{PATH}txt_files/consolidated_parser_output.txt"
PROCESSED_PARSER_OUTPUT_FILE = f"{PATH}txt_files/parser-output.txt"

