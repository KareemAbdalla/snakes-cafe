print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
""")

menu = {
'Wings': 0,
'Cookies': 0,
'Spring Rolls': 0,
'Salmon': 0,
'Steak': 0,
'Meat Tornado': 0,
'A Literal Garden': 0,
'Ice Cream': 0,
'Cake': 0,
'Pie': 0,
'Coffee': 0,
'Tea': 0,
'Unicorn Tears': 0,
}

orders = {}
while True:
    print("** What would you like to order? ** \n ***********************************")
    order = input('>')

    if order == "quit":
        break

    elif order not in menu:
        print("please select items from the menu")

    elif order not in orders and order in menu:
        orders[order] = 1
        print(f"** {orders[order]} order of {order} have been added to your meal **")


    elif order in orders:
        orders[order] += 1
        print(f"** {orders[order]} orders of {order} have been added to your meal **")

if len(orders) != 0:
    print(orders)

else:
    print("No Items Were Selected!!!")


