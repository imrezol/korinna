# https://www.w3schools.com/python/python_scope.asp

age = 30

def my_func():
    age = 20
    print("age inside my_func", age)

def my_func2():
    age = 20
    print("age inside my_func2", age)
    if 1==1 :
        age = 10
        print("age inside if", age)
    print("age inside my_func2 after if", age)

def my_func3():
    price = 200
    print("price inside my_func3", price)


my_func()

print("age outside my_func", age)

my_func2()

# print("price outside my_func2", price) # NameError: name 'price' is not defined