# def fun(num):
#     return num * num 

fun = lambda num : num * num
result = fun(5)
print(result)

# gum = lambda n : 
# result = gum(4)
# print(result)


num = int(input("Enter the number:"))
validate = lambda n : "Even" if num % 2 == 0 else "Odd"

print(validate(num))