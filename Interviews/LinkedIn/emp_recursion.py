import requests

def get_employee_hierarchy(employee_id, indent_level=0):
    response = requests.get(f"http://www.employee.com/api/employee/{employee_id}")
    print(response)
    if response.status_code != 200:
        print(f"Error fetching employee {employee_id}")
        return
    employees = response.json()
    indent = " " * indent_level
    print(f"{indent}{employees['name']} - {employees['title']}")

    for report_id in employees['reports']:
        get_employee_hierarchy(report_id, indent_level+1)

get_employee_hierarchy('A123456789')