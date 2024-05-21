#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    name = sys.argv[1]
    tt = 0
    nt = 0
    com_task = []

    user = "https://jsonplaceholder.typicode.com/users/{}".format(name.json())

    response1 = requests.get(user)
    r1 = response1.json()
    user_Id = r1["id"]

    todo = "https://jsonplaceholder.typicode.com/todos/"
    response2 = requests.get(todo)
    r2 = response2.json()

    if (response1 and response2):

        for key in r2:

            if key["userId"] == user_Id:
                tt += 1
                if key['completed'] is True:
                    nt += 1
                    com_task.append(key['title'])

        print(f"Employee {r1['name']} is done with tasks ({nt}/{tt}):")

        for task in com_task:
            completed_task = ""
            completed_task = "\t {}".format(task)
            print(completed_task)

    else:
        print(f"Error: {response.status_code}")
