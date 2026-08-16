#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    employee_tasks = [
        task for task in todos
        if task.get("userId") == employee_id
    ]

    completed_tasks = [
        task for task in employee_tasks
        if task.get("completed")
    ]

    total_tasks = len(employee_tasks)
    number_done = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_done,
            total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
