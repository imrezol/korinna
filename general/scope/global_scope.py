# https://www.w3schools.com/python/python_scope.asp

fruit = "apple"

def my_func():
    global fruit
    fruit = "orange"
    print("fruit inside my_func", fruit)

def my_func2():
    global name
    name = "Korinna"
    print("name inside my_func2", name)



print("fruit before my_func", fruit)
my_func()
print("fruit after my_func", fruit)

my_func2()
print("name outside my_func2", name) # without calling my_func2: NameError: name 'name' is not defined
