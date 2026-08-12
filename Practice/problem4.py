# reverse a string with for loop

def reverse_string(str):
    reversed_string = ""

    for i in str:
        reversed_string = i + reversed_string
    return reversed_string

str = "Code"
print(reverse_string(str))

name = "Srimathi"[::-1]
print(name)