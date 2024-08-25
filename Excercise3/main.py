employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

def print_employee_info(employees):
    for employee in employees:
        print(f"Name: {employee['name']}\nJob: {employee['job']}\nCity: {employee['address'].get('city')}\n")

def print_country_second_employee(employees):
    second_employee = employees[1]
    country_second_employee = second_employee["address"]["country"]
    print(f"Country of second employee: {country_second_employee}")

print_employee_info(employees)
print_country_second_employee(employees)
