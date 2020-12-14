print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************\n')
print('Appetizers')
print('----------')
print('Wings')
print('Cookies')
print('Spring Rolls\n')
print('Entrees')
print('-------')
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A Literal Garden\n')
print('Desserts')
print('--------')
print('Ice Cream')
print('Cake')
print('Pie\n')
print('Drinks')
print('------')
print('Coffee')
print('Tea')
print('Unicorn Tears\n')
print('***********************************')
print('** What would you like to order? **')
print('***********************************')

orders = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}

# attribution for getting rid of multiple prints using found flag: https://stackoverflow.com/questions/20157108/if-else-statement-and-dictionary-in-python

while True:
        user_input = input('> ')
        if user_input == "quit":
            break
        found = False
        for (key, value) in orders.items():
            if key == user_input and value == 0:
                orders[key] += 1
                totalamount = orders[key]
                print('\n** ' + str(totalamount) + ' order of %s' % (key) + ' have been added to your meal **\n')
                found = True
            # if more than 1 item, display "orders" instead of "order"
            elif key == user_input:
                orders[key] += 1
                totalamount = orders[key]
                print('\n** ' + str(totalamount) + ' orders of %s' % (key) + ' have been added to your meal **\n')
                found = True
                break
        # stretch goal - only allow ordering items on the menu & allow ordering items not on menu but give custom reply
        if not found:
            print("That item is not available. Please order something from the menu!")

# stretch goal - print out a summary of complete order
print('Here is a summary of your complete order:')
found = False
for (key, value) in orders.items():
    if orders[key] >= 1:
        print(key, value)
        found = True
if not found:
    print("Nothing in cart. Please add a menu item.")

          
