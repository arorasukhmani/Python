# A module is file containing a set of functions to include in your application

import datetime
import time

today = datetime.date.today()
print(today)

timestamp = time.time()
print(timestamp)

# import datetime
# from datetime import date
# today = date.today()

# pip freeze shows all the installed modules

# Pip module
from camelcase import CamelCase

c= CamelCase()
print(c.hump('Hello there people'))

# import custom module
import validator
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')

email1 = 'test#test.com'
if validate_email(email1):
    print('Email is valid')
else:
    print('Email is not valid')