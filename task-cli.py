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

def update_file():
    with open("tasks.json", 'w') as f:
        f.write(json.dumps(tasks))

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
        update_file()
        print(f"{args[2]} added successfully!")
    case "update":
        if len(args) != 4:
            print("Please enter the ID as well as the new task name.")
            print("e.g. python task-cli update 1 \"Buy groceries\"")
            quit(1)
        for t in tasks:
            if str(t["id"]) == args[2]:
                t["description"] = args[3]
                update_file()
                print(f"Task {t["id"]} updated successfully!")
                quit(0)
        print("Task not found. Make sure you input a valid ID. ")
        print("e.g. python task-cli update 1 \"Buy groceries\"")
        quit(1)