import json
import os

JSON_FILE = "tasks.json"  

def load_tasks():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_tasks(task_list):
    with open(JSON_FILE, "w") as file:
        json.dump(task_list, file, indent=4)
