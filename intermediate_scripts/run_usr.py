from discourse_mapped_rel import USR
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from modules.set_path import PATH

n = len(sys.argv)

#input_dir = "bulk_USRs/"
input_dir = f"{PATH}txt_files/bulk_USRs"
output_dir = f"{PATH}txt_files/bulk_USRs_mod"
input_mode = 0

if input_dir == "":
    input_dir = "./test"    #change to data storage location
if output_dir == "":
    output_dir = "./results_test"    #change to result storage location

usr = USR()
usr.set_root_folder_path(input_dir)
usr.set_res_folder_path(output_dir)
usr.set_input_mode(input_mode)    # set input mode == 0 for single root folder
                                                                # in case root folder contains sub folders, use input mode 1
usr.run()
