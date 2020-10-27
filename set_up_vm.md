# Setting up a Notram VM
This guide explains a standard setup of a VM for BERT training. It installs the necessary dependencies and sets up a few necessary tools. It also clones the Notram-github and the Notram-branch of the CT-BERT-github. If you are connecting as a new user to an existing VM you will have to run most of these steps as well.

## Get some general tools and generate the public key
```bash
sudo apt-get install ssh git tmux wget
#Useful since the public key can be added to git repositories ("Setting" - "Deploy keys")
#Replace email address
ssh-keygen -t rsa -C "per@capia.no"
```

## Install Conda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
#Answer “yes” to the last question
```
After this you will have to close and reopen connection.

## Create a conda environment and auto restart it
```bash
conda create -n python36 python=3.8 (Creates a Python 3.8 environment called python38)
echo "conda activate python38" >> ~/.bashrc (Sets the default environment)
```
Close and reopen connection. When logging in the command line should state “python38”

## Set up git credentials
```bash
#Replace name and email
git config --global user.name "Per E Kummervold" 
git config --global user.email "per@capia.no"
#Make sure username and password will then be stored globally after first login
git config --global credential.helper store```
```

## Clone Notram
```bash
git clone https://github.com/NBAiLab/notram.git
pip install -r notram/requirements.txt
python -m spacy download nb_core_news_sm (if you get errors try: spacy download nb_core_news_sm)
```

## Clone CT-bert and checkout Notram branch 
Please note that the CT-BERT has a lot of requirements, including Tensorflow. If you are not installing this library, you should in any case install the requirements.

```bash
git clone https://github.com/digitalepidemiologylab/covid-twitter-bert.git
cd covid-twitter-bert
git checkout notram
git submodule update --init
cd ..
pip install -r covid-twitter-bert/requirements.txt
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

