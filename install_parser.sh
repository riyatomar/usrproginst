
# Installation of tokenizer
git clone https://irshadbhat@bitbucket.org/iscnlp/tokenizer.git
cd tokenizer
sudo python3 setup.py install
pip3 install -r requirements.txt
cd ..
echo "tokenizer installed"
echo "===================="

# Installation of pos-tagger
git clone https://irshadbhat@bitbucket.org/iscnlp/pos-tagger.git
cd pos-tagger
sudo python3 setup.py install
pip3 install -r requirements.txt
mv isc_tagger ../
cd ..
echo " pos-tagger installed"
echo "===================="

# Installation of parser
git clone https://irshadbhat@bitbucket.org/iscnlp/parser.git
cd parser
sudo python3 setup.py install
pip3 install -r requirements.txt
mv isc_parser ../
cd ..
echo "parser insatlled"
echo "===================="