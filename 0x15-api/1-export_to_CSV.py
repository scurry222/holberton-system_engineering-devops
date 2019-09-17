#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """

if __name__ == '__main__':

    import requests
    from sys import argv
    import csv

    f_name = argv[1] + ".csv"

    with open(f_name, 'w', newline='') as f:
        user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
        name = requests.get(user).json().get('name')
        req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
        request = requests.get(req)
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for req in request.json():
            w.writerow([argv[1], name, str(req.get('completed')),
                       req.get('title')])
