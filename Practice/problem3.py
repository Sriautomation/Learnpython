#Print all numbers from 1 to 100 that are divisible by 3 or 5.

for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)