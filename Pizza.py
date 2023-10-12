class Pizza:                                             #Pizza Class
    def __init__(self, size, price, numberofpizzas):        #Data Fields
        self.size = size
        self.price = price
        self.numberofpizzas = numberofpizzas
    
    def total(self):                                #Total method
        self.price = self.price * self.numberofpizzas
        if self.numberofpizzas >= 3:
           self.price = self.price * 0.85
        return self.price
       

    def __str__(self):                         #Obect info or str method
        return f'''You have ordered {self.numberofpizzas} {self.size} pizzas
        Your total after discount is $ {self.price}
        '''