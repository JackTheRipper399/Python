# Python reading files (.txt, .json, .csv)

import json
import csv

# file_path = "pythonLessons/output.txt"
# file_path = "pythonLessons/output.json"
file_path = "pythonLessons/output.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        # print(content)
        # print(content["name"])
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
