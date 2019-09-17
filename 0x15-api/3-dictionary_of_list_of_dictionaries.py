#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """

if __name__ == '__main__':

    from requests import get
    import json

    d = {}
    for user_id in range(1, 11):
        user = get("https://jsonplaceholder.typicode.com/users/{}"
                   .format(user_id))
        name = user.json()
        req = get("https://jsonplaceholder.typicode.com/todos?userId={}"
                  .format(user_id))
        todos = req.json()

        d[user_id] = [dict(task=todo['title'], completed=todo['completed'],
                           username=name['username']) for todo in todos]

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(d))
