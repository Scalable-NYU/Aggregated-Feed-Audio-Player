# Aggregated Feed Audio Player
## Introduction

## Get Started
0. **Prerequisit**

Please first install python3, pip3, and virtualenv

1. **Install dependencies**

The original library is already created so you only need to add new packages in it. In *cc_radio_flask_1.0* directory, run the following to install existing packages:

```
pip install -r requirements.txt
```
Install new packages (ex. flask) and add to requirements.txt
```
pip install flask
pip freeze > requirements.txt
```
2. **Warning**

Virtualenv does not support spaces in the path, which means such paths will be ignored and virtualenv will search for system python libraries.

## Run

1. **Twitter**

Run the following code to start the app
```
export OAUTHLIB_INSECURE_TRANSPORT=1
python app.py
```
Then go to [localhost:5000](localhost:5000)