def exit_program(num_total_calculations):
    print(f"number of total calculations: {num_total_calculations}")
    print("Thank you for using the Calculator program, bye bye!")
    exit(0)

def is_number(input_number):
    return input_number is not None and input_number.isdigit()


def reset_values(a, b, c):
    a = None
    b = None
    c = None

def is_valid_operation(operation):
    valid_operations = ["plus", "minus", "multiply", "divide"]
    return operation is not None and operation in valid_operations

def is_exit(text):
    return text is not None and text == "exit"

def perform_calculation(a, b, operation):
    first_number = int(a)
    second_number = int(b)
    if operation == "plus":
        return first_number + second_number
    elif operation == "minus":
        return first_number - second_number
    elif operation == "multiply":
        return first_number * second_number
    elif operation == "divide":
        return first_number / second_number
