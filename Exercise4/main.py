from helper import get_youngest_employee, count_lower_and_upper, print_even_numbers_from_list

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
},
{
  "name": "Sole",
  "age": 31,
  "birthday": "1993-07-28",
  "job": "Developer",
  "address": {
    "city": "Milan",
    "country": "Italy"
  }
}]

get_youngest_employee(employees)
count_lower_and_upper("AbCd")
print_even_numbers_from_list([1, 2, 3, 4, 5, 6])
