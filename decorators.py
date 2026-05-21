
def log_deco(func):
    def wrap(a,b):
        print("Values", a , "", b)
        result = func(a,b)
        print("Result", result)
        return result   
    return wrap

def greater_first(func):
    def wrap(a,b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrap

@greater_first
def sub(a,b):
    # if a < b:
    #     a, b = b, a
    return a - b

@greater_first
def divide(a,b):
    # if a < b:
    #     a, b = b, a
    return a / b

# sub = greater_first(sub)
# divide = greater_first(divide)

result1 = sub(2, 4)
print(result1)
result2 = divide(4, 2)
print(result2)
