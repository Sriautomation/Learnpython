data = [1,  "Sri", 2, "Uj", 3]
 
for value in range(10):
    # if value % 3 == 0:
    #     continue
    if value == 5:
        break
    
    print(value)

print("End of the program")

for num in range(10):
    if num % 3 == 0:
        continue
    if num == 8:
        break
    print(num)