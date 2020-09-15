import json

with open("hobbies.json", "r") as f:
    data = json.load(f)
    name = data["firstName"]
    seperate = ", "
    activity = seperate.join(data["hobbies"])
    print(name, f"has hobbies as {activity}")