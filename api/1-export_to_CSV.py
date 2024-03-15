#!/usr/bin/python3
"""
"""


import requests
import sys
import csv


def get_employee_tasks(employee_id):
    """ function returns employee to do list information """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos".format(base_url)

    employee_data = requests.get(employee_url).json()
    specific_employee = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    tasks = []
    for todo in todo_list:
        task = {
            "USER_ID": employee_id,
            "USERNAME": specific_employee,
            "TASK_COMPLETED_STATUS": "Completed" if todo["completed"] else "Incomplete",
            "TASK_TITLE": todo["title"]
        }
        tasks.append(task)
    return tasks

def export_to_csv(tasks, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASKS_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)

if __name__ == "__main__":
    get_employee_tasks(int(sys.argv[1]))
    export_to_csv(filename="USER_ID.csv")