employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

def update_job_title(new_title):
    employee["title"] = new_title

def remove_age():
    employee.pop("age")

def print_dict():
    for key in employee.keys():
        print(f"{key}: {employee[key]}")

update_job_title("Software Engineer")
remove_age()
print_dict()

dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}
unified_dict = {}

def merge_dicts(a, b):
    for k, v in a.items():
        unified_dict[k] = v
    for k, v in b.items():
        unified_dict[k] = v
    return unified_dict

def sum_all_values(d):
    sum = 0
    for k, v in d.items():
        sum += v
    return sum

def get_min_and_max(d):
    min_value = min(d.values())
    max_value = max(d.values())
    return min_value, max_value

print(f"unified dic: {merge_dicts(dict_one, dict_two)}")
print(f"sum of all values within dictionary: {sum_all_values(unified_dict)}")
print(f"min and max: {get_min_and_max(unified_dict)}")
