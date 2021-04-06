"""
kata link: https://www.codewars.com/kata/5d23d89906f92a00267bb83d  
Instruction : Some new cashiers started to work at your restaurant.

They are good at taking orders, but they don't know how to capitalize words, or use a space bar!

All the orders they create look something like this:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.

Their preference is to get the orders as a nice clean string with spaces and capitals like so:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

The kitchen staff expect the items to be in the same order as they appear in the menu.

Code:"""
def get_order(order):
    order_list = []
    menu = {
        1: "Burger",
        2: "Fries",
        3: "Chicken",
        4: "Pizza",
        5: "Sandwich",
        6: "Onionrings",
        7: "Milkshake",
        8: "Coke"
    }
    for item in menu.values():
        if item.lower() in order:
            while order_list.count(item) != order.count(item.lower()):
                order_list.append(item)
    return " ".join(order_list)
            