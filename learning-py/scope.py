name = "this var in global"

print("Global scope variable:", name)


def my_func():
    print("1. Local scope variable:", name)


my_func();


def my_func2():
    name = "this var in func2"
    print("2. Local scope variable:", name)

    def my_func3():
        name = "this var in func3"
        print("2.1 Local scope variable:", name)

    my_func3()


my_func2()
print("Global scope variable:", name)

# variables are not scoped inside loops or conditional statements
# this is not like javaScript where variables are block scoped

for char in "soumil":
    last_name = "roy"
    print(char)

if True:
    message = "I'm in if block"

print("Global scope variable:", last_name)  # roy
print("Global scope variable:", char)  # l
print("Global scope variable:", message)  # I'm in if block
