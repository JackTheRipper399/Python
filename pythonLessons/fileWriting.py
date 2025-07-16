# Python writing files (.txt, .json, .csv)

import json
import csv

# employee = {
#    "name": "Spongebob",
#    "age": 30,
#    "job": "cook"
# }

employees = [["Name", "Age", "Job"],
             ["Sponebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "pythonLessons/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        # json.dump(employee, file, indent=4)
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
