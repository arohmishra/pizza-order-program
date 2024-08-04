print("Hiiiii.....")
want_pizza = input("do you want pizza(Y/N) ?")
price = 0
pepporoni_price = 0
bill = 0 
if want_pizza == 'Y' or want_pizza == 'y':
    pizza_size = input("which size of pizza you want (S/M/L)?")
    if pizza_size == 'S' or pizza_size == 's' :
        price = 100
        print("price for small pizza is 100")
    elif pizza_size == 'M' or pizza_size == 'm' :
        price = 200
        print("price for medium pizza is 200")
    elif pizza_size == 'L' or pizza_size == 'l' :
        price = 300
        print("price for large pizza is 300")    
    else:
        print("sorry! no such size of pizza is on us.")    

    pepporoni = input("do you want pepporoni(Y/N)?")
    if pepporoni == 'Y' or pepporoni == 'y':
        if pizza_size == 'S' or pizza_size == 's' :
            pepporoni_price = 30
            price = price + 30
            print(f"your bill is {price}")
        elif pizza_size == 'M' or pizza_size == 'm' or pizza_size == 'L' or pizza_size == 'l':
            pepporoni_price = 50
            price = price + 50
            print(f"your bill is {price}")  
    cheese = input("do you want cheese(Y/N)?")
    if cheese == 'Y' or cheese == 'y':
        bill = price + 20
        print(f"your total bill is {bill}")
        print("Thank you...enjoy your pizza😊.")
                   
else:
    print("thank you! come again..")


