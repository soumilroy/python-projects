numbers = [1, 2, 3, 4, [5, 6, 7, 8, [9, 10, 11, 12]]]

print(numbers)  # [1, 2, 3, 4, [5, 6, 7, 8, [9, 10, 11, 12]]]
print(len(numbers))  # 5
print(numbers[3])  # 4
print(numbers[4])  # [5, 6, 7, 8, [9, 10, 11, 12]]
print(numbers[4][0])  # 5
print(numbers[4][2])  # 7
print(numbers[4][4])  # [9, 10, 11, 12]
print(numbers[4][4][3])  # 12

star_war_chars = [
    ['Darth', 'Vader'],
    ['Luke', 'Skywalker'],
    ['Han', 'Solo'],
]

print(star_war_chars[2][1])  # Han Solo
print(star_war_chars[0][1])  # Han

for row in star_war_chars:
    for character in row:
        print(character)
