import sys
import os
import json
import datetime
args = sys.argv


if len(args) == 1:
    print("Please enter some arguments. e.g. python task-cli add \"Buy groceries\"")
    quit(1)

if not os.path.exists("tasks.json"):
    _ = open("tasks.json", mode="w")

with open("tasks.json") as file:
    try:
        tasks = json.loads(file.read())
    except json.decoder.JSONDecodeError:
        tasks = []

match args[1]:
    case "add":
        if len(args) != 3:
            print("Please enter which task you would like to add.")
            quit(1)
        curr = {
                "id": len(tasks) + 1,
                "description": args[2],
                "status": "todo",
                "createdAt": datetime.datetime.now().strftime("%c"),
                "updatedAt": datetime.datetime.now().strftime("%c")
        }
        tasks.append(curr)
        with open("tasks.json", 'w') as file:
            file.write(json.dumps(tasks))
        print(f"{args[2]} added successfully!")