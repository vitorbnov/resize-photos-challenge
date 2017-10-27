# Resize Photos - Challenge

This project is an implementation of this challenge:

https://s3.amazonaws.com/sample-login/attachments/files/000/000/304/original/ResizePhoto.pdf

## Why use Python?

Python is a general-purpose programming language that provides developers building many kinds of applications and has a growing community that helps improving it's ecosystem. In addition, it's easy to build and run.

## Instructions

First of all we need to install the requirements (python 2.7 and pymongo 3.5)

`$ pip install -r requirements.txt`

To run web app in development mode:

`$ uwsgi development.ini --py-autoreload 1`

You must have a MongoDB server running locally in order to run this application in development mode

To run some unit tests:

`$ python tests/photos_resizer_test.py`
