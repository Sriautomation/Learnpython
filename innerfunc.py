
def outer():
    print("This is a outer function")
    def inner(num):
        print("This is a inner function", num)
    return inner

result = outer()    
result(5)