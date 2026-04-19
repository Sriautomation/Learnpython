
a = 10

def validate():
    a = 15
    globals()['a'] = 20
    print("Inside value of a is : ", a)

validate()
print("Outside value of a is: ", a)


# program

x = 20
def update():
    x = 10
    print("Inside func: ", x)

update()
print("Outside func: ", x)