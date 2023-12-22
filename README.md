1. Create a virtual environment inside the "usrproginst" folder by running the following commands:
	>>> cd usrproginst
	>>> python3 -m venv venv
	>>> source venv/bin/activate


2. Install iscnlp tokenizer, pos-tagger and parser by running the following script:
	>>> sh install_parser.sh
	
		
3. Files and folders creation: 
	>>> After installing, create a input file named "sentences_for_USR" that contains Hindi Sentence/sentences with their respective IDs separated by double space.
			Eg. 123  राम खाना खाता है |
	>>> Now create one folder within "usrproginst" folder named "txt_files" and a text file named "bh-1" inside the same folder for the generation of single USR.
	>>> Create two folder named "bulk_USRs" and "bulk_USRs_mod" in the "usrproginst folder" for bulk generation.
	>>> Also create one text file named "bh-2" within "usrproginst" folder for temporary use.


4. Run the following commands on terminal inside usrproginst folder:
	>>> sudo apt install python3
	>>> sudo snap install curl
	>>> curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
	>>> sudo python3 get-pip.py
	>>> sudo apt-get install python-requests
	>>> sudo bash install-project.sh


5. To run the NER model, install the transformers and torch using following commands:
	>>> pip3 install transformers
	>>> pip3 install torch
	if any error occurred then run this:
		>>> pip3 install transformers[torch]
		

6. Run the following commands to compile the morph dictionary after the installation of apertium and lttoolbox:
	>>>	sudo apt-get update
    >>> sudo apt-get install lttoolbox
    >>> sudo apt-get install apertium
	>>> sh compile_dict.sh


7. Run the following command to install wxconv:
	>>> pip3 install WXC
	>>> pip3 install wxconv
			

8. Copy wx_utf8, utf8_wx and ir_no@ files to bin folder:
	>>> cd /usr/bin/
	>>> sudo cp ~/usrproginst/wx_utf8 .
	>>> sudo cp ~/usrproginst/utf8_wx .
	>>> sudo cp ~/usrproginst/ir_no@ .


9. Change the permissions of wx_utf8, utf8_wx and ir_no@ files:
	>>> sudo chmod +777 utf8_wx
	>>> sudo chmod +777 wx_utf8 
	>>> sudo chmod +777 ir_no@		


10. Run the following commands within usrproginst to install the tool for updating concepts :
	>>> sudo apt-get -f install apertium-all-dev
	>>> apt-cache policy | grep apertium
	>>> sudo apt-get install python3-openpyx		
	>>> lt-comp lr apertium-eng.eng.dix eng.bin


===================================================================
Steps for Generating concept row:
(i) Keep the Hindi sentence in the bh-1 file within "txt_files" folder
(ii) Run the following command on the terminal:
	>>> python3 generate_concept_row.py
To generate rest of the rows, run the following command:
	>>> python3 row3_to_row11.py

===================================================================
Steps for Generating concept row in bulk:
(i) Keep the Hindi sentences in "sentences_for_usr" file with their respective IDs seperated with double space.
(ii) Run the following command on the terminal:
	>>> python3 generate_bulk_concept.py
Output will be stored in "bulk_USRs" folder. 

===================================================================
Run the following commands to generate different row in bulk:

[1] Concept row: python3 generate_bulk_concept.py
[2] Index row: python3 generate_bulk_index.py
[3] Sementic Category row: python3 generate_bulk_sem_cat.py
[4] Morpho Sementic row: python3 generate_bulk_morph_sem.py
[5] Dependency row: python3 generate_bulk_dependency.py
[6] Discourse row: python3 generate_bulk_discourse.py
[7] Speaker View row: python3 generate_bulk_spk_view.py
[8] Scope row: python3 generate_bulk_scope.py
[9] Sentence Type row: python3 generate_bulk_sent_type.py



   
