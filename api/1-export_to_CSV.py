#!/usr/bin/python3
""" this module utilizes an API
 to return information on employees tasks
"""


import csv
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

    tasks = []
    for todo in todo_list:
        task = {
             "USER_ID": employee_id,
             "USERNAME": specific_employee,
             "TASK_COMPLETED_STATUS": "Completed" if todo["completed"]
             else "Incomplete",
             "TASK_TITLE": todo["title"]
        }
        tasks.append(task)
    return tasks


def export_to_csv(tasks, filename):
    """function for exporting employee task info to csv file"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [task['USER_ID'], task['USERNAME'],
                   task['TASK_COMPLETED_STATUS'], task['TASK_TITLE']]
            writer.writerow(row)


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    employee_tasks = get_employee_tasks(user_id)
    filename = f"{user_id}.csv"
    export_to_csv(employee_tasks, filename)
