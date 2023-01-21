# JSON is commonly used with data APIS
# parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "Joe", "last_name": "King", "age": 28}'

# Parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# Dict to json
car = {'make': 'Ford','model': 'Mustang', 'year': 1975}
carJSON = json.dumps(car)
print(carJSON)