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
fruit_prices = {
    "apple": 1.25,
    "banana": 3.45,
    "orange": 2.75,
}

fruit_name = input("Enter fruit name: ")
found_product = fruit_prices.get(fruit_name)  # returns None if not found

if found_product:
    print(f"Price of {fruit_name} is {found_product}")
else:
    print("Sorry, we don't have that product")
    print(found_product)
