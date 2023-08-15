# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules (way 1)
# import datetime

# today = datetime.date.today()
# print(today)

from datetime import date

today = date.today()
print(today)

# Way 1
# import time

# print(time.time())

# Way 2
from time import time

print(time())

# pip freeze -> show all libraries

# Custom modules
# import validator
from validator import validate_email

email = "test#test.com"
if validate_email(email):
    print("succeeded!")
else:
    print("not an email")
