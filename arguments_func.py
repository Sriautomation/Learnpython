#default argument

def sum(a, b):
    return a + b

result = sum(5, 6)
print(result)

#variable length argument

def add(num1, *num2):
    dumb = num1
    for n in num2:
        dumb += n
    return dumb

value = add(4, 5, 6, 7)
print(value)

#keyword arguments

def person(name, **kwlargs):
    print("name :", name)
    #print("age :", age)
    for k,v in kwlargs.items():
        print(k, ":", v)


achiever = person(name = "Sri", age = "18", loc = "Blr", tech = "python")

def greet(name, msg="welcome to telusko!"):
    print("hello", name, msg)

greet("navin")
greet("Harsh", "Good to see you again!")
