#!/usr/bin/python3
""" this module utilizes an API
 to return information on employees tasks
"""

import json
import requests
import sys


def get_employee_tasks(employee_id):
    """ function returns employee to do list information """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos".format(base_url)

    employee_data = requests.get(employee_url).json()
    specific_employee = employee_data['username']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

    tasks = {
        str(employee_id): [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": specific_employee
            } for todo in todo_list
        ]
    }
    return tasks


def export_to_json(tasks, filename):
    """function for exporting employee task info to csv file"""
    with open(filename, 'w') as jsonfile:
        json.dump(tasks, jsonfile)


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    employee_tasks = get_employee_tasks(user_id)
    filename = f"{user_id}.json"
    export_to_json(employee_tasks, filename)
