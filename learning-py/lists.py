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
    star_war_characters)  # ['Han Solo', 'C-3PO', 'R2-D2', 'Chewbacca', 'Luke Skywalker', 'Leia Organa', 'Obi-Wan Kenobi']
