# similar to arrays, Lists are ordered collection of values

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3])  # 4
print(numbers[-1])  # 10
print(numbers[3:6])  # [4, 5, 6]

# Lists can have any type of data

rand_data = [1, "soumil", True, 3.14, []]
print(rand_data)  # [1, 'soumil', True, 3.14, []]

print(list('SOUMIL'))  # ['S', 'O', 'U', 'M', 'I', 'L']

numbers[3] = -12.4
print(numbers)  # [1, 2, 3, -12.4, 5, 6, 7, 8, 9, 10]
print(len(numbers))  # 10

# numbers[11] = 11 # out of range error
# print (numbers)

# List methods
# append
numbers.append(342)  # adds 342 to the end of the list
print(numbers)  # [1, 2, 3, -12.4, 5, 6, 7, 8, 9, 10, 342]

# extend
# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

negative_numbers = [-3, -2, -1]
numbers.extend(negative_numbers)
print(numbers)  # [1, 2, 3, -12.4, 5, 6, 7, 8, 9, 10, 342, -3, -2, -1]

# Insert element at a specific index

star_war_characters = ['Han Solo', 'C-3PO', 'R2-D2', 'Luke Skywalker', 'Leia Organa', 'Obi-Wan Kenobi']

star_war_characters.insert(3, 'Chewbacca')
print(
    star_war_characters)  # ['Han Solo', 'C-3PO', 'R2-D2', 'Chewbacca', 'Luke Skywalker', 'Leia Organa', 'Obi-Wan
# Kenobi']

# Slicing lists # list[start:stop:step]
print("SOUMILROY"[6:9])  # ROY
print(star_war_characters[4:])  # ['Luke Skywalker', 'Leia Organa', 'Obi-Wan Kenobi']
print(star_war_characters[1:7:2])  # ['C-3PO', 'Chewbacca', 'Leia Organa']
print(star_war_characters[::2])  # ['Han Solo', 'R2-D2', 'Luke Skywalker', 'Obi-Wan Kenobi']

# replacing sliced lists
star_war_characters[1:3] = ["Vader", "Mando", "Moff Gideon"]  # ['Han Solo', 'Vader', 'Mando', 'Chewbacca', 'Luke
# Skywalker',
# 'Leia Organa', 'Obi-Wan Kenobi']
print(star_war_characters)

# Clear list - remove all values from lists
# star_war_characters.clear()
# print(star_war_characters)

star_war_characters.remove("Moff Gideon")
print(star_war_characters)

