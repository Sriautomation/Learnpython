# def square(num):
#     return num * num

# def cube(num):
#     return num * num * num

# #higher order function, since it is accepting another function
# # def operate(num, operation):
# #     return operation(num)

# def operate(nums, operation):

#     for i in nums:
#         result4 = operation(i)
#         print(result4)

# # value = 5
# # result = square(value)
# # result2 = cube(value)
# # result3 = operate(value, square)
# nums = [5, 6, 7]
# operate(nums, cube)
# print(result, result2)
# print(result3)


#program

def square(num):
    return num * num
def operate(num, operation):
    
    for i in num:
        result = operation(i)
        print(result)


num = [3, 4, 5]
operate(num, square)

