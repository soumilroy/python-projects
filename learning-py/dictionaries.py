detective = {
    "name": "Sherlock Holmes",
    "email": "sherlock@gmail.com",
    "age": 54,
    "is_verified": True,
    "address": "125 Baker Street",
    "city": "London",
    "country": "UK",
    "phone": "0123456789",
    "cases": ["The Blind Banker", "The Hounds of Baskerville"],
    False: "WTF?",
    False: "WTF again?",
    666: "Call Satan?",
    # [1]: "Test"
}
print(type({}))  # dict
print(detective)  # dump the dictionary
print(detective["name"])  # get a value from a key
print(detective["cases"])  # get a value from a key
print(detective[False])  # "WTF again?" Keys overwritten
print(detective[666])  # Call Satan?
# print(detective[[1]])  # Wont work - unhashable type: 'list'


# get
# fruit_prices = {
#     "apple": 1.25,
#     "banana": 3.45,
#     "orange": 2.75,
# }

# fruit_name = input("Enter fruit name: ")
# found_product = fruit_prices.get(fruit_name)  # returns None if not found

# if found_product:
#     print(f"Price of {fruit_name} is {found_product}")
# else:
#     print("Sorry, we don't have that product")
#     print(found_product)

# Iterate over a dictionary
# dict.keys(), dict.values(), dict.items()

print(detective.keys())  # dict_keys(['name', 'email' ....])

print(detective.values())  # dict_values(['Sherlock Holmes', '

print(type(detective.keys()))  # dict_keys, iterable but not list

print(type(detective.values()))  # dict_values, iterable but not list

# To convert to list

print(list(detective.keys()))  # ['name', 'email' ...] - true list

for ch in detective.keys():
    print(ch)  # list of keys

for ch in detective.values():
    print(ch)  # list of values

# To retrieve all the items (key, value pairs)

# dict_items([('name', 'Sherlock Holmes'), ('email', '
print(detective.items())  # tuples

for key, value in detective.items():
    print(f"{key} -- {value}")  # key, value pairs
