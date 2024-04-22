#!/usr/bin/python3
"""
Script to retrieve and display information about an employee's TODO listprogres
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    todo_response = requests.get("{}/todos?userId={}".format
                (base_url, employee_id))

    if user_response.status_code != 200:
        print("Error: Could not retrieve user data")
        sys.exit(1)

    if todo_response.status_code != 200:
        print("Error: Could not retrieve TODO list data")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = [task["title"]
                for task in todo_data if task["completed"]]

    print("Employee {} is done with tasks({}/{}):".format
                (employee_name, len(completed_tasks), total_tasks))
    for task_title in completed_tasks:
        print("\t", task_title)
