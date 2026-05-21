class mobile:
    def __init__(self, cpu, ram, storage):
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    #cpu = "i7" # class variable
    def iphone(self):
        #print("Specification: 6GB RAM, 128GB Storage")
        print("Specification:", self.cpu, self.ram, self.storage)
    
mistblue = mobile("i7", "12GB", "2TB")
hazegrey = mobile("13", "16GB", "5TB")

#mobile.iphone(mistblue)
mistblue.iphone()
hazegrey.iphone()

#print(mistblue.cpu)
#print(mistblue.cpu)

class Device:
    def __init__(self, name):
        print("init called for:", name)
        self.name = name.upper()
    
    def show(self):
        print("Device :", self.name)

d1 = Device("laptop")
d2 = Device("mobile")

d1.show()
d2.show()