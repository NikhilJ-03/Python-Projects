menu={
    "Coffee": 60,
    "Pasta": 120,
    "Sandwich": 80,
    "Burger": 40,
    "Salad": 100 
}
print("Namaste sir, welcome to out PYHTON Restraunt")
response=input("would you like to order something. (Yes/No):")
ordertotal=0
if response=="Yes":
    print('''Coffee: 60
Pasta: 120
Sandwich: 80
Burger: 40
Salad: 100''')
    item1=input("What would you like to order: ")
    if item1 in menu:
        ordertotal=ordertotal+menu[item1]
    else:
        print('Sorry sir it is not  in our menu')
    another_order=input("Do you want to order anyhting else (Yes/No): ")
    if another_order=="Yes":
        item2=input("Yes sir what you like to have: ")
        if item2 in menu:
            ordertotal=ordertotal+menu[item2]
        else:
            print('Sorry sir it is not  in our menu')
    else:
        ("Okay no problem.")
    print(f"Your order total is {ordertotal}\nThank You!")
else:
    print("Get lost then.")