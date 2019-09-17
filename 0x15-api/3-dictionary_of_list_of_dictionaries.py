#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """

import json
import requests
from sys import argv


if __name__ == '__main__':

    users = "https://jsonplaceholder.typicode.com/users"
    length = len(requests.get(users).json())
    f_name = "todo_all_employees.json"

    all_todos = {}

    with open(f_name, 'w') as f:
        for user in range(1, length + 1):
            u = requests.get(users + "/" + str(user))
            name = u.json().get('username')
            all_todos[user] = []
            todos = "https://jsonplaceholder.typicode.com/todos?"
            url = todos + str(user)
            r = requests.get(url)
            for task in r.json():
                all_todos[user].append({"task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": name})
        json.dump(all_todos, f)
