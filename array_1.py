import array
from array import *

arr = array('i',[11,22,33,44,55])

#print(arr.tolist())

for n in arr:
    print(n)




#Program
float_arr = array('f', [2.5, 4.8, -3.2, 6.7])
for n in float_arr:
    if n < 0:
        continue
    print(n)

arr_func = array('i', [10, 20, 30])
arr_func.append(40)
arr_func.reverse()
print(arr_func[0])


from array import *
length = int(input('Enter length of array: '))
arr1 = array('i', [])
for i in range(length):
    x = int(input('Enter next value: '))
    arr1.append(x)
print(arr1)