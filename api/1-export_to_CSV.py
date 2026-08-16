#!/usr/bin/python3
"""Export employee data to CSV format.

Given an employee ID, this script queries a REST API
(https://jsonplaceholder.typicode.com), fetches that
employee's TODO list, and exports every task record to
a CSV file named <employee_id>.csv.

Usage:
    ./1-export_to_CSV.py <employee_id>
"""
import csv
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

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
