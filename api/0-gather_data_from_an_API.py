#!/usr/bin/python3
""" module for utilizing API to retrieve todo list info on employee """


import requests
import sys


def get_employee_todo(employee_id):
    """ function returns employee to do list information """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos".format(base_url)

    employee_data = requests.get(employee_url).json()
    specific_employee = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()
    todo_json = todo_list.json()

    complete_todos = []
    total_todos = 0
    for todo in todo_json:
        total_todos += 1
        if todo["completed"] is True:
            complete_todos.append(todo["title"])

    print("Employee {} is done with tasks{}/{}:".format(
        specific_employee, len(complete_todos), total_todos))
    for task_title in complete_todos:
        print("\t{} {}".format(task_title, '\t'))

if __name__ == "__main__":
    get_employee_todo(int(sys.argv[1]))
