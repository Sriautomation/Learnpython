import sys

# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())

# count = 1
# def greet():
#     global count
#     print("Hello", count)
#     count = count + 1
#     greet()

# greet()


#Program
#Write a python program to print numbers from 1 to 10 without any Loop 
#Use an if condition to stop the recursion when the number becomes greater than 10

# number = 1
# def num():
#     global number
#     print(number)
#     number = number + 1
#     if number > 10:
#         return number
#     num()
# num()


# def num(number):
#     print(number)
#     number+=1
#     if number > 10:
#         return number
#     num(number)
# num(1)

def sum(number, total):
    print(number)
    number+=1
    if number > total:
        return total
    sum(number, total)
    
result = sum(1, 50)
