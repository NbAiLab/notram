# Setting up a Notram VM
This guide explains a standard setup of a VM for BERT training. It installs the necessary dependencies and sets up a few necessary tools. It also clones the Notram-github and the Notram-branch of the CT-BERT-github. If you are connecting as a new user to an existing VM you will have to run most of these steps as well.

## Get some general tools and generate the public key
```bash
sudo apt-get install ssh git tmux wget locales byobu jq

#Having Nordic Characters might be handy. Run this script and install the languages you need. Make sure you have nb_NO.utf8 and nn_NO.utf8 installed.
sudo dpkg-reconfigure locales

#Then you might switch locale by this command. You might have to log in and out of the ssh for this to take effect. 
sudo update-locale LC_ALL="nb_NO.utf8"

#Replace email address with your git email address and press ENTER on all questions
ssh-keygen -t rsa -C "per@capia.no"
```
After the public key is generated it will tell you the placement. This might be a good time to add this to the git repositories under "Setting" - "Deploy keys" if you plan on pushing changes to the git.

## Install Conda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

```
After you have answered "yes" to the last question you still have to close and reopen connection.

## Create a conda environment and auto restart it
```bash
conda create -n python38 python=3.8 
echo "conda activate python38" >> ~/.bashrc 
```
Close and reopen connection. When logging in the command line should state “python38”

## Set up git credentials
```bash
#Replace name and email
git config --global user.name "Per E Kummervold" 
git config --global user.email "per@capia.no"
#Make sure username and password will then be stored globally after first login
git config --global credential.helper store
```

## Clone Notram
```bash
git clone https://github.com/NBAiLab/notram.git
pip install -r notram/requirements.txt
python -m spacy download nb_core_news_sm
```

## Clone CT-bert and checkout Notram branch 
Please note that both the Notram and CT-BERT has a lot NLP-tools as requirements, including Tensorflow. It might be useful running the requirements-file even if you do not clone the libraries. 

```bash
git clone https://github.com/digitalepidemiologylab/covid-twitter-bert.git
pip install -r covid-twitter-bert/requirements.txt
cd covid-twitter-bert
git checkout notram
git submodule update --init
cd ..

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
Congratulations! You now have a clean VM image set up with all necessary authentications. If you plan on setting up multiple VMs this might be a good time to save this image in the [Google Cloud Console](https://console.cloud.google.com/).
