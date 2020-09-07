# https://www.w3schools.com/python/python_scope.asp

age = 30

def myfunc():
    age = 20
    print("age inside myfunc", age)

def myfunc2():
    age = 20
    print("age inside myfunc", age)
    if 1==1 :
        age = 10
        print("age inside if", age)
    print("age inside myfunc after if", age)

def myfunc3():
    price = 200
    print("price inside myfunc3", price)


myfunc()

print("age outside myfunc", age)

myfunc2()

# print("price outside myfunc2", price) # NameError: name 'price' is not defined