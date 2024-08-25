import datetime as d

user_input = input("Hi there! When is your birthday? (format: dd/mm/yyyy)\n")
birthday = d.datetime.strptime(user_input, "%d/%m/%Y")
now = d.datetime.now()
delta = birthday - now
days_left = delta.days
hours_left = int((delta.total_seconds() / 3600) % 24)
minutes_left = int((delta.total_seconds() / 60) % 60)
print(f"Your birthday is in {days_left} days, {hours_left} hours, and {minutes_left} minutes.")
