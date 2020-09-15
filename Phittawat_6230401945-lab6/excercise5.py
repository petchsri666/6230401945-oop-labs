import json

data = { "firstName": "Jane",
    "lastName": "Doe",
     "hobbies": ["running", "sky diving", "singing"]}


with open("hobbies.json", "w")as f:
    json.dump(data, f)

with open("hobbies.json", "r") as i:
    print(json.load(i))