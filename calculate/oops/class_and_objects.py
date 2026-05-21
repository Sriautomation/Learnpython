class mobile:
    def iphone(self):
        print("Specification: 6GB RAM, 128GB Storage")
    
mistblue = mobile()
mobile.iphone(mistblue)
mistblue.iphone()

input = 10
print(type(input))

# class laptop:
#     def HP(self):
#         print("RAM: 16GB")
#     def Dell(self):
#         print("RAM: 8GB")

# l1 = laptop()
# l2 = laptop()
# laptop.HP(l1)
# laptop.Dell(l2)
# l1.HP() 
# l2.Dell()

class laptop:
    def details(self, brand, ram):
        self.brand = brand
        self.ram = ram
        print(brand, ram)

l1 = laptop()
l1.details("HP", "16GB")
l2 = laptop()
l2.details("Dell", "8GB")