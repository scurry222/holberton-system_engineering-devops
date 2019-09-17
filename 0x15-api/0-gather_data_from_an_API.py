#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """

import requests
from sys import argv


if __name__ == '__main__':

    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(user).json().get('name')
    req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    request = requests.get(req)

    total = [task for task in request.json()]
    completed = [task for task in request.json() if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(total)))
    for task in completed:
        print("\t {}".format(task.get('title')))
