#!/usr/bin/python3
"""
Script to retrieve and export information about an employee's TODO list
progress in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    todo_response = requests.get("{}/todos?userId={}".format(
        base_url, employee_id))

    if user_response.status_code != 200:
        print("Error: Could not retrieve user data")
        sys.exit(1)

    if todo_response.status_code != 200:
        print("Error: Could not retrieve TODO list data")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["username"]
    csv_file = "{}.csv".format(employee_id)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
            "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([employee_id, employee_name,
                str(task["completed"]), task["title"]])

    print("CSV file '{}' has been created successfully.".format(csv_file))
