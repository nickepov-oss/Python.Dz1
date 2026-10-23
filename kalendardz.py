from datetime import datetime
birthday_input = input("Enter your birth date (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_input, "%Y-%m-%d")
today = datetime.today()
next_birthday = birthday.replace(year=today.year)
days_left = (next_birthday - today).days

print(" Days until your birthday:", days_left)