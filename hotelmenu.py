
menu ={
    'pizza':40,
    'pasta':120,
    'maggie':60,
    'chilli potato':50,
    'honey chilli potato':60,
    'tea':10,
    'coffee':80,
    'salad':70,
}

print(menu)

#greet
print("welcome to tongue twister Restaurant")
print("pizza: Rs40\n pasta: Rs120\n maggie: Rs60\n chilli potato: Rs60\n honey chilli potato: Rs80\n tea: Rs10\n coffee: Rs80\n salad: Rs70\n")

order_total = 0
#80 + 70 = 150

item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"your item {item_1}has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet!")
another_order = input("do you want to add another item? (yes/No)")
if another_order =="yes":
    item_2 =input("enter the name of the second item =")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not avialable!")

print(f"the total amount of items is to pay {order_total}")                  