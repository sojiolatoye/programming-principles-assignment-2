from User import User
from Pizza import Pizza  





name1 = input("What is your name?")
email1 = input("What is your email address?")
address1 = input("What is your  address?")

u = User(name1, email1, address1)
u1 = (u.name,u.email, u.address)


size1 = input("What size pizza would you like Small/Medium/Large/X-Large?")
if size1 == "Small":
   print("One pizza of this size is $10")
elif size1 == "Medium": 
   print("One pizza of this size is $12")
elif size1 == "Large":
    print("One pizza of this size is $15")
elif size1 == "X-Large":
    print("One pizza of this size is $18")


price1 = 0

if size1 == "Small":
    price1 = 10
elif size1 == "Medium":
    price1 = 12
elif size1 == "Large":
    price1 = 15
elif size1 == "X-Large":
    price1 = 18


numberofpizzas1 = int(input("How many pizzas of this size would you like to order?"))

p = Pizza(size1, price1, numberofpizzas1)
p1 =(p.size, p.total(), p.numberofpizzas)

print(p)
print('''Order will be delivered to''',u.name,''' at''',u.address,'''
        Receipt will be emailed to ''',u.email,)
