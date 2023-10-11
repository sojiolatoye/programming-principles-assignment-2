from User import User, Pizza

u = User()
p = Pizza()

u.name = input("What is your name?")
u.email = input("What is your email address?")
u.address = input("What is your  address?")



p.size = input("What size pizza would you like Small/Medium/Large/X-Large?")
if p.size == "Small":
    print("One pizza of this size is $10")
elif p.size == "Medium": 
    print("One pizza of this size is $12")
elif p.size == "Large":
    print("One pizza of this size is $15")
elif p.size == "X-Large":
    print("One pizza of this size is $18")
p.numberofpizzas= int(input("How many pizzas of this size would you like to order?"))

u = User()
p = Pizza()