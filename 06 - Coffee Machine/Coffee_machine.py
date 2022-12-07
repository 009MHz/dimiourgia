from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Todo 0: assigning the called classes into variable
menu = Menu()
coffee_bot = CoffeeMaker()
cashier = MoneyMachine()

# Todo 1: creating the loops to activate / deactivate the machine
machine_on = True
while machine_on:
    # Todo 1a: calling the coffee item
    coffee = menu.get_items()
    # Todo 1b: prompt to user action
    prompt = input(f"""\nType "off" to turn off the machine
Type "report" to generate the current report
Type these items: [{coffee}] to order?\n""").lower()

    # Todo 2: Follow up the action on user prompt
    # Todo 3: Turning off the machine and breaking the loop
    if prompt == "off":
        print("\nMachine is shutting down...")
        machine_on = False

    # Todo 4: Generating the report for the resources and the money
    elif prompt == "report":
        coffee_bot.report()
        cashier.report()

    # Todo 5: Processing the user order
    else:
        # Calling the menu order instance
        order = menu.find_drink(prompt)
        # Passing the instance for checking the resource
        if coffee_bot.is_resource_sufficient(order):  #hasilnya sudah Boolean
            # Check the order cost >< user money
            if cashier.make_payment(order.cost):
                # (order.cost) is instantly calling the cost attributes under Menu Class

                # Creating the coffee
                coffee_bot.make_coffee(order)