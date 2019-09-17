#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """

import json
import requests
from sys import argv


if __name__ == '__main__':

    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(user).json().get('name')
    req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    request = requests.get(req)
    f_name = argv[1] + ".json"

    with open(f_name, 'w') as f:
        d = {argv[1]: []}
        for r in request.json():
            d.get(argv[1]).append({"task": r.get('title'),
                                   "completed": r.get('completed'),
                                   "username": name})
        json.dump(d, f)
