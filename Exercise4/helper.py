def get_youngest_employee(dict):

    # get the age of the younges employee(s)
    min_age = 1000
    for employee in dict:
        employee_age = employee["age"]
        if employee_age < min_age:
            min_age = employee_age

    print("The youngest employees are:")
    for employee in dict:
        if employee["age"] == min_age:
            print(f"- {employee['name']}, {employee['age']} years old")

def count_lower_and_upper(text):
    lower_count = 0
    upper_count = 0
    for letter in text:
        if letter.isupper():
            upper_count += 1
        else:
            lower_count += 1
    print(f"{lower_count} lower and {upper_count} upper case letters")

def print_even_numbers_from_list(list):
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append(number)
    print(f"List with even numbers only: {even_list}")
