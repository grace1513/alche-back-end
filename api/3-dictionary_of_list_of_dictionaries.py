#!/usr/bin/python3
"""Export all employees' data to JSON format.

This script queries a REST API (https://jsonplaceholder.typicode.com)
for every employee and their TODO list, then exports all of it to a
single JSON file named todo_all_employees.json.

Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(base_url))
    users_data = users_response.json()

    todos_response = requests.get("{}/todos".format(base_url))
    todos_data = todos_response.json()

    all_employees = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for task in todos_data:
            if task.get("userId") == user_id:
                tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        all_employees[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees, json_file)
