# https://www.w3schools.com/python/python_scope.asp

fruit = "apple"

def myfunc():
    global fruit
    fruit = "orange"
    print("fruit inside myfunc", fruit)

def myfunc2():
    global name
    name = "Korinna"
    print("name inside myfunc2", name)



print("fruit before myfunc", fruit)
myfunc()
print("fruit after myfunc", fruit)

myfunc2()
print("name outside myfunc2", name) # without calling myfunc2: NameError: name 'name' is not defined
