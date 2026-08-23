import argparse
import json
from pathlib import Path

if Path('tasks.json').exists():
    with open("tasks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
else:
    data = {"tasks":[]}
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")


parser_create = subparsers.add_parser("add")
parser_create.add_argument("value")

parser_update = subparsers.add_parser("update")
parser_update.add_argument("id", type=int)
parser_update.add_argument("value")

parser_delete = subparsers.add_parser("delete")
parser_delete.add_argument("id", type=int)

parser_list = subparsers.add_parser("list")
parser_list.add_argument("value", nargs="?")

args = parser.parse_args()

if args.command == "add":
    lista = []
    id = 0
    if len(data["tasks"]) == 0:
        id = 1
    else:
        for task in data["tasks"]:
            lista.append(task["id"])
        id = max(lista) + 1
    
    task_value = {"id": id, "task": args.value}
    data["tasks"].append(task_value)
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)
    print("task created")

elif args.command == "update":

    for task in data["tasks"]:
        if args.id == task["id"]:
            task["task"] = args.value
            print("task updated")
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

elif args.command == "delete":

    for task in data["tasks"]:
        if args.id == task["id"]:
            data["tasks"].remove(task)
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            break

elif args.command == "list":

    if args.value == None:
        for task in data["tasks"]:
            print(task["task"])