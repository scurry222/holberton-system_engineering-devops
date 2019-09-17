#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """

import json
import requests
from sys import argv
import csv


if __name__ == '__main__':
    if len(argv) != 2:
        exit(1)

    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(user).json().get('name')
    req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    request = requests.get(req)
    f_name = argv[1] + ".csv"

    with open(f_name, 'w', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for req in request.json():
            w.writerow([argv[1], name, str(req.get('completed')),
                       req.get('title')])
