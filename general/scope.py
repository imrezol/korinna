# https://www.w3schools.com/python/python_scope.asp

x = 300

def myfunc3():
    global z
    z = "Korinna"
    print("z inside myfunc3", z)


def myfunc2():
    y = 200
    print("y inside myfunc", y)

def myfunc():
    x = 200
    print("x inside myfunc", x)
    if 1==1 :
        x = 100
        print("x inside if", x)
    print("x inside myfunc after if", x)

myfunc()

print("x outside myfunc", x)
# print("y outside myfunc2", y) # NameError: name 'y' is not defined
myfunc3()
print("z outside myfunc3", z) # without calling myfunc3: NameError: name 'z' is not defined