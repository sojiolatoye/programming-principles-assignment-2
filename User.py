class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
class Pizza:
    def __init__(self, size, price, numberofpizzas):
        self.size = size
        self.price = price
        self.numberofpizzas = numberofpizzas
    
    def total(self):
        return self.price
    
    def __str__(self):
        return 
