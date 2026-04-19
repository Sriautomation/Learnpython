
def fact(num):
    if num == 1:
        return 1
     
    return num * fact(num-1)

result = fact(5)
print(result)

#Program

def fact(n):
    if n == 0:
        return 0
    return n * fact(n-1)

res = fact(4)
print(res)