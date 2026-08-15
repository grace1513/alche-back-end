#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )

    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = employee.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]
    number_done = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_done, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
