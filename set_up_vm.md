# Setting up a Notram VM
This guide explains a standard setup of a VM for BERT training. It installs the necessary dependencies and sets up a few necessary tools. It also clones the Notram-github and the Notram-branch of the CT-BERT-github. If you are connecting as a new user to an existing VM you will have to run most of these steps as well.

## Get some general tools and generate the public key
```bash
sudo apt-get install ssh git tmux wget (requires sudo-access. Not really required for the other steps)
ssh-keygen -t rsa -C "per@capia.no". (Optional. The public key can be added to git repositories for push - Settings-Deploy keys)
```

## Install Conda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
#Answer “yes” to the last question
#Close and reopen connection.
```


## Create a conda environment and auto restart it
```bash
conda create -n python36 python=3.8 (Creates a Python 3.8 environment called python38)
echo "conda activate python38" >> ~/.bashrc (Sets the default environment)
#close and reopen connection. When logging in the command line should state “python38”
```

## Set up git credentials
```bash
#Replace name and email
git config --global user.name "Per E Kummervold" 
git config --global user.email "per@capia.no"
#Make sure username and password will then be stored globally after first login
git config --global credential.helper store```
```

## Clone notram
```bash
git clone https://github.com/NBAiLab/notram.git
pip install -r notram/requirements.txt
python -m spacy download nb_core_news_sm (if you get errors try: spacy download nb_core_news_sm)
```

## Clone covid-bert and checkout Notram branch 
```bash
git clone https://github.com/digitalepidemiologylab/covid-twitter-bert.git
cd covid-twitter-bert
git checkout notram
git submodule update --init (This library builds on the tensorflow library. Installed as a submodule here)
cd ..
pip install -r covid-twitter-bert/requirements.txt (Most likely everything is already installed here)
```

## Install GCloud and authenticate
```bash
#Install GCloud if necessary
curl https://sdk.cloud.google.com | bash
source ~/.bashrc

gcloud auth login
gcloud auth application-default login 

#You might have to change to another project for billing and access
gcloud config set project nancy-194708

```

