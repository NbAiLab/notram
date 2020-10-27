Setting up a Conda Environment for Norwegian Transformer Model

List of machines
meta2.lx.nb.no
35.228.238.109
sveinb.nb.no


Get some general tools and generate the public key
sudo apt-get install ssh git tmux wget (requires sudo-access. Not really required for the other steps)
ssh-keygen -t rsa -C "per@capia.no". (Optional. The public key can be added to git repositories for push - Settings-Deploy keys)

Install Conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
Answer “yes” to the last question
Close and reopen connection.

Create a conda environment and auto restart it
conda create -n python36 python=3.6 (Creates a Python 3-6 environment called python36)
echo "conda activate python36" >> ~/.bashrc (Sets the default environment)
close and reopen connection. When logging in the command line should state “python36”

Set up git credentials
git config --global user.name "Per E Kummervold" (Your name… sic)
git config --global user.email "per@capia.no" (Your email… sic)
git config --global credential.helper store (Username and password will then be stored globally after first login)


Clone alto-tools (not used?)
git clone https://github.com/cneud/alto-tools.git

Clone notram
git clone https://github.com/NBAiLab/notram.git
pip install -r notram/requirements.txt
python -m spacy download nb_core_news_sm (if you get errors try: spacy download nb_core_news_sm)

Clone covid-bert
git clone https://github.com/digitalepidemiologylab/covid-twitter-bert.git
cd covid-twitter-bert
git submodule update --init (This library builds on the tensorflow library. Installed as a submodule here)
cd ..
pip install -r covid-twitter-bert/requirements.txt (Most likely everything is already installed here)

Set login credentials Gcloud (Really useful for having the correct credentials)
gcloud auth login
gcloud auth application-default login 
gcloud config set project nancy-194708 (Use this to change to another project - billing and access)

Install GCloud if necessary (only do this if the above commands leads to an error)
curl https://sdk.cloud.google.com | bash
source ~/.bashrc


