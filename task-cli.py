import sys
import os
import json
args = sys.argv


if len(args) == 1:
    print("Please enter some arguments. e.g. python task-cli add \"Buy groceries\"")
    quit(1)

if not os.path.exists("tasks.json"):
    _ = open("tasks.json", mode="w")

with open("tasks.json") as file:
    tasks: dict = json.loads(file.read())

match args[1]:
    case "add":
        if len(args) != 2:
            print("Please enter which task you would like to add.")