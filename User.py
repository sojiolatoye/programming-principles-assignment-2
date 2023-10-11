from pizzaapp import u, p 
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
class Pizza:
    def __init__(self, size = "Small, Medium, Large, X-Large", price = "10, 12, 15, 18", numberofpizzas = []):
        self.size = size
        self.price = price
        self.numberofpizzas = numberofpizzas
    
    def total(self):
        self.price = self.size + self.numberofpizzas
        if p.numberofpizzas >= 3:
            (self.price / 15) + self.price
        return self.price


    def __str__(self):
        return f'''You have ordered {self.numberofpizzas} {self.size} pizzas
        Your total after discount is {self.price}
        Order will be delivered to {u.name} at {u.address}
        Receipt will be emailed to {u.email}'''
