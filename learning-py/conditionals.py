# if statement block is indentation based
# How are you perceived in society
age = input("How old are you? ")

if not age:
	print("You didn't enter your age!")
	exit()

age = int(age);

if age < 18:
	print("You are a minor.")
elif age < 21:
	print("You are a youth.")
elif age < 65:
	print("You are an adult.")
else:
	print("You are senior citizen.")