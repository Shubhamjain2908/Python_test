import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Curreynt age is ", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is ", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Shubham", "age": 21}
    print("No file found , default age is ", data["age"])

old_file.seek(0)        # reset the file
old_file.write(json.dumps(data))