#!/usr/bin/python3
"""Export employee data to JSON format.

Given an employee ID, this script queries a REST API
(https://jsonplaceholder.typicode.com), fetches that
employee's TODO list, and exports every task record to
a JSON file named <employee_id>.json.

Usage:
    ./2-export_to_JSON.py <employee_id>
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, "w") as json_file:
        json.dump({employee_id: tasks}, json_file)
