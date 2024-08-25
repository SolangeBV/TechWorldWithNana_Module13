my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
filtered_list = []

def filter_numbers_higher_than(input_number):
    try:
        for number in my_list:
            if number > int(input_number):
                filtered_list.append(number)
        print(f"This is the filtered list: {filtered_list}")
    except Exception:
        print("Some error occurred, please make sure you enter an integer number")

print(f"This is my_list: {my_list}")
user_input = input("Enter an integer number and I will give you\n all the numbers within my_list that are higher than that number\n")
filter_numbers_higher_than(user_input)
