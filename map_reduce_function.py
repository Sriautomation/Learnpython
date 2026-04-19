from functools import reduce

# nums = [4,3,6,7,8,4]
# #evens = []
# # def double_it(n):
# #     return n * 2
# # def sum_it(a,b):
# #     return a + b

# evens = list(filter(lambda n : n % 2 == 0, nums))
# #doubles = list(map(double_it, evens))
# doubles = list(map(lambda n : n * 2, evens))
# #sum = reduce(sum_it, doubles)
# sum = reduce(lambda a,b : a + b, doubles)

# print(evens)
# print(doubles)
# print(sum)

lst = [2, 3, 4]

# def cube_it(n):
#     return n ** 3
# def sum_it(a,b):
#     return a + b

#cubes = list(map(cube_it, lst))
#cubes = list(map(lambda n : n ** 3, lst))
#sum = reduce(sum_it, cubes)
sum = reduce(lambda a,b : a + b, list(map(lambda n : n ** 3, [2, 3, 4])))

#print(cubes)
print(sum)


