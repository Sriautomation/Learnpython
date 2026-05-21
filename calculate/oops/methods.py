class mobile:
    brand = "Apple" # class variable
    def __init__(self, cpu, ram, storage):
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
    #cpu = "i7" # class variable
    def iphone(self):
        #print("Specification: 6GB RAM, 128GB Storage")
        print("Specification:", self.cpu, self.ram, self.storage)
    @classmethod
    def info(cls):
        return cls.brand
    @staticmethod
    def gb_to_bytes(gb):
        return gb * 1024 * 1024 * 1024

    
mistblue = mobile("i7", "12GB", "2TB")
hazegrey = mobile("13", "16GB", "5TB")

mistblue.iphone()
hazegrey.iphone()
print(mobile.info())
print(mobile.gb_to_bytes(8))