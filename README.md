# Aggregated Feed Audio Player
## Introduction

## Initiate Flask
0. **Prerequisit**

Please first install python3, pip3, and virtualenv

1. **Install dependencies**

The original library is already created so you only need to add new packages in it. In *cc_radio_flask_1.0* directory, run the following to install existing packages:

```
$ pip install -r requirements.txt
```
Install new packages (ex. flask) and add to requirements.txt
```
$ pip install flask
$ pip freeze > requirements.txt
```
2. **Warning**

Virtualenv does not support spaces in the path, which means such paths will be ignored and virtualenv will search for system python libraries.

## Deployment on AWS
1. **Connect to AWS EC2**

```
$ chmod 400 ccProject.pem
$ ssh -i ccProject.pem ubuntu@ec2-54-90-73-104.compute-1.amazonaws.com
```
2. **Install dependencies** 

Similar to working on local machine, create virtual environment and install dependencies

3. **Set locale**

When you run 
```
$ pip install -r requirements.txt
```
It may run into **locale.Error: unsupported locale setting** issue. To solve this, run following command:
```
$ export LC_ALL="en_US.UTF-8"
$ export LC_CTYPE="en_US.UTF-8"
```

4. **Run**
```
$ python app.py
```
Public IP is: 54.90.73.104

## Resource:

- https://sysadmins.co.za/interfacing-amazon-dynamodb-with-python-using-boto3/  
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.02.html  
- https://www.datasciencebytes.com/bytes/2015/02/28/using-flask-to-answer-sql-queries/  
- https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/  
