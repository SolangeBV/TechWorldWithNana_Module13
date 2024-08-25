from helper import reset_values, is_number, is_valid_operation, is_exit, exit_program, perform_calculation

print("Hello! This is a calculator program. It will run until you input 'exit'")
num_total_calculations = 0

while True:
  while True:
    a = input("Enter first number:\n")
    if is_number(a):
      break
    elif is_exit(a):
      exit_program(num_total_calculations)
    else:
      print("Please enter a valid number.")

  while True:
    b = input("Enter second number:\n")
    if is_number(b):
      break
    elif is_exit(b):
      exit_program(num_total_calculations)
    else:
      print("Please enter a valid number.")

  while True:
    c = input("Enter operation (eg: plus, minus, multiply, divide):\n")
    if is_valid_operation(c):
      break
    elif is_exit(c):
      exit_program(num_total_calculations)
    else:
      print("Please enter a valid operation.")

  result = perform_calculation(a, b, c)
  num_total_calculations += 1
  print(f"The result of your calculation is: {result}\n")
  print("That was fun! Let's do this again.")
  reset_values(a, b, c)
