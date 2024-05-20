#!/usr/bin/python3
"""Write a Python script that, using this REST API"""

if __name__ == "__main__":
    import sys
    import requests
    import json

    name = sys.argv[1]
    num_task++;

    user = "https://jsonplaceholder.typicode.com/users/{}".format(name)

#    response1 = requests.get(user)
#    res1 = response1.json()
#    user_Id = res1["id"]

    todo = "https://jsonplaceholder.typicode.com/todos/"
    response2 = requests.get(todo)
    res2 = response2.json()

    if (response1 and response2):

        print(res1)
        print(res2)
        #print("Employee {} is done with tasks".format(res1["name"]))
        #print(userId)

        for key, value in res2.items():
            if key == userId and value == user_Id:
                num_task++;

        #Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):EMPLOYEE_NAME: name of
    else:
        print(f"Error: {response.status_code}")

