import argparse
import json
from pathlib import Path
from datetime import datetime

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

parser_mark_done = subparsers.add_parser("mark-done")
parser_mark_done.add_argument("id", type=int)

parser_mark_in_progress = subparsers.add_parser("mark-in-progress")
parser_mark_in_progress.add_argument("id", type=int)

parser_update = subparsers.add_parser("update")
parser_update.add_argument("id", type=int)
parser_update.add_argument("value")

parser_delete = subparsers.add_parser("delete")
parser_delete.add_argument("id", type=int)

parser_list = subparsers.add_parser("list")
parser_list.add_argument("value", nargs="?")

parser_test = subparsers.add_parser("test")

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
    
    task_value = {"id": id, "description": args.value, "status": "todo", "createdAt": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "updatedAt": None}
    data["tasks"].append(task_value)
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)
    print("task created")

elif args.command == "update":

    for task in data["tasks"]:
        if args.id == task["id"]:
            task["description"] = args.value
            task["updatedAt"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("tasks.json", "w") as f:
                 json.dump(data, f, indent=4)
            print("task updated")

elif args.command == "delete":

    for task in data["tasks"]:
        if args.id == task["id"]:
            data["tasks"].remove(task)
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            print("task deleted")
            break

elif args.command == "list":

    if args.value == None:

        if len(data["tasks"]) > 0:
            
            for task in data["tasks"]:
                print(f'ID: {task["id"]}')
                print(f'{task["description"]}')
                print(f'Status:{task["status"]}')
                print(f'Criado:{task["createdAt"]}')
                if task["updatedAt"] != None:
                    print(f'Atualizado:{task["updatedAt"]}')
                print("")
        else: 
            print("No tasks found")

    elif args.value == "todo":
        for task in data["tasks"]:
            if task["status"] == args.value:
                print(f'ID: {task["id"]}')
                print(f'{task["description"]}')
                print(f'Status:{task["status"]}')
                print(f'Criado:{task["createdAt"]}')
                if task["updatedAt"] != None:
                    print(f'Atualizado:{task["updatedAt"]}')
                print("")
            else:
                print("No 'todo' tasks found")
    elif args.value == "done":
            for task in data["tasks"]:
                if task["status"] == args.value:
                    print(f'ID: {task["id"]}')
                    print(f'{task["description"]}')
                    print(f'Status:{task["status"]}')
                    print(f'Criado:{task["createdAt"]}')
                    if task["updatedAt"] != None:
                        print(f'Atualizado:{task["updatedAt"]}')
                    print("")
                else: 
                    print("No 'done' tasks found")

    elif args.value == "in-progress":
            for task in data["tasks"]:
                if task["status"] == args.value:
                    print(f'ID: {task["id"]}')
                    print(f'{task["description"]}')
                    print(f'Status:{task["status"]}')
                    print(f'Criado:{task["createdAt"]}')
                    if task["updatedAt"] != None:
                        print(f'Atualizado:{task["updatedAt"]}')
                    print("")
                else: 
                    print("No 'in-progress' tasks found")


elif args.command == "mark-in-progress":
    for task in data["tasks"]:
        if args.id == task["id"]:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            print("task marked as in-progress")
            

elif args.command == "mark-done":
    for task in data["tasks"]:
        if args.id == task["id"]:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)
            print("task marked as done")
            

elif args.command == "test":
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
