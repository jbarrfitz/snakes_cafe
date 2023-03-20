def main():
    menu = """**************************************
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
Unicorn Tears"""
    order_prompt = """***********************************
** What would you like to order? **
***********************************"""
    curr_order = {'wings': 0,
                  'cookies': 0,
                  'spring rolls': 0,
                  'salmon': 0,
                  'steak': 0,
                  'meat tornado': 0,
                  'a literal garden': 0,
                  'ice cream': 0,
                  'cake': 0,
                  'pie': 0,
                  'coffee': 0,
                  'tea': 0,
                  'unicorn tears': 0}
    print(menu)
    print(order_prompt)
    entry = input("> ").lower()
    while entry != "quit":
        if entry in curr_order.keys():
            curr_order[entry] += 1
            if curr_order[entry] == 1:
                print(f"{curr_order[entry]} order of {entry.title()} has been added to your order")
            else:
                print(f"{curr_order[entry]} orders of {entry.title()} have been added to your order")
        else:
            print("I'm sorry, but we don't offer that item.")
        entry = input("> ").lower()
    print("***************************")
    print("Your order summary:")
    ordered_items = 0
    for key, value in curr_order.items():
        if value > 0:
            ordered_items += 1
            print(f"{key.title()}: {value}")
    if ordered_items == 0:
        print("No items ordered")
    print("***************************")
    print("Thank you for visiting Snakes Cafe")


if __name__ == "__main__":
    main()
