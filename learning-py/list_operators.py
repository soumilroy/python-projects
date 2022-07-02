# concatenate lists [12, 13, 14, 15, 16, 17]
print([12, 13, 14] + [15, 16, 17])

# TypeError: can only concatenate list (not "int") to list
# print([12, 13, 14] + 5)

# Multiply lists
# [12, 13, 14, [21, 22, 23], 12, 13, 14, [21, 22, 23], 12, 13, 14, [21, 22, 23]]
print([12, 13, 14, [21, 22, 23]] * 3)
print([1, 2, 3, 1, 1] * 5)  # [1, 2, 3, 1, 1, 1, 1, 1, 1, 1]

# Check if value is present in list
list = [1, "Soumil", "soumil@gmail.com",
        ["Kolkata", "Shimla", "Delhi"], 1, 4, 5, 6, 5, 2, 5]

print(1 in list)  # True
print("Soumil" in list)  # True
print("soumil@yahoo.com" in list)  # False
print("Kolkata" in list)  # False
print("Delhi" in list[3])  # True

# Count number of times a value is present in list else return 0
# list.count takes 1 arg else throws error
print(list.count(1))  # 2
print(list.count(5))  # 3
print(list.count(123))  # 0

print([1, 2] == [1, 2])  # True
print([1, 2] == [1, 2, 3])  # False
print([1, 2] == [2, 1])  # False

num1 = [1, 2, 3]
num2 = [1, 2, 3]
num3 = num2

print(num1 == num2)  # True
print(num1 is num2)  # False
print(num2 is num3)  # True
