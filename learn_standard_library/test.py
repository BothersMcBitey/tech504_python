import this

import math

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
# gives us remainder of the 2 values# 5 can't go into 1, so the remainder is 1print(f"Remainder from 1/5: {math.remainder(1, 5)}")

import os

# returns our current working directory
working_directory = os.getcwd()
print(f"Current working directory: {working_directory}")
username = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"The current user is: {username}")
cpu_cores = os.cpu_count()
print(f'Total CPU cores: {cpu_cores}')
# change directory - must exist
# os.chdir("<folder_name>")
# make a new directory
os.mkdir("Cheese")

import sys
# gives us the current paths important to the Python interpreter
print(f"Current path: {sys.path}")

print(sys.version)

import datetime
#gives us today's date
print(f"Today's date: {datetime.date.today()}")
whatisthedate = datetime.datetime.now()
print(whatisthedate)

import requests

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)