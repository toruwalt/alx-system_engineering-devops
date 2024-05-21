#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    name = sys.argv[1]
    total_task = 0
    num_task = 0
    com_task = []

    user = "https://jsonplaceholder.typicode.com/users/{}".format(name)

    response1 = requests.get(user)
    res1 = response1.json()
    user_Id = res1["id"]

    todo = "https://jsonplaceholder.typicode.com/todos/"
    response2 = requests.get(todo)
    res2 = response2.json()

    if (response1 and response2):

        for key in res2:
            
            if key["userId"] == user_Id:
                total_task += 1
                if key['completed'] == True:
                    num_task += 1
                    com_task.append(key['title'])
                    #print("\t {}".format(key['title']))

        
        print("Employee {} is done with tasks ({}/{}):".format(res1["name"], num_task, total_task))

        for task in com_task:
            completed_task = ""
            completed_task = "\t {}".format(task)
            print(completed_task)

    else:
        print(f"Error: {response.status_code}")

