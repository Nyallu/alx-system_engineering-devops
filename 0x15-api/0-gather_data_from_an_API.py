#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} employee_id".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]
base_url = "https://jsonplaceholder.typicode.com"

# Get employee information
response = requests.get("{}/users/{}".format(base_url, employee_id))
employee = response.json()
employee_name = employee["name"]

# Get employee's tasks
response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
tasks = response.json()

# Count the number of completed tasks
completed_tasks = [task for task in tasks if task["completed"]]
num_completed_tasks = len(completed_tasks)

# Print the progress report
print("Employee {} is done with tasks({}/{}):".format(
    employee_name, num_completed_tasks, len(tasks)))

for task in completed_tasks:
    print("\t {}".format(task["title"]))

