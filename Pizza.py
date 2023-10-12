class Pizza:
    def __init__(self, size, price, numberofpizzas):
        self.size = size
        self.price = price
        self.numberofpizzas = numberofpizzas
    
    def total(self):
        self.price = self.price * self.numberofpizzas
        if self.numberofpizzas >= 3:
           self.price = self.price * 0.85
        return self.price
       

    def __str__(self):
        return f'''You have ordered {self.numberofpizzas} {self.size} pizzas
        Your total after discount is $ {self.price}
        '''