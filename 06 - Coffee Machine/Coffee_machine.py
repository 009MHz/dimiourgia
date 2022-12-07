from menu import Menu, MenuItem
from coffee_maker import Brain
from money_machine import MoneyMachine

menu = Menu()
coffee_bot = Brain()
cashier = MoneyMachine()

# Creating the loops to activate / deactivate the machine
machine_on = True
while machine_on:
    # Activating the item menu
    coffee = menu.get_items()
    # Prompt to user action
    prompt = input(f"""\nType "off" to turn off the machine
Type "report" to generate the current report
Type these items: [{coffee}] to order?\n""").lower()

    """machine response based user prompt"""
    # Turning off the machine and breaking the loop
    if prompt == "off":
        print("\nMachine is shutting down...")
        machine_on = False

    # Generating the report for the resources and the money
    elif prompt == "report":
        coffee_bot.report()
        cashier.report()

    # Processing the user order
    else:
        # Handling invalid input
        order = menu.find_drink(prompt)
        # Checking the resource based on user order
        if coffee_bot.is_resource_sufficient(order):
            # Check the order cost >< user money
            if cashier.make_payment(order.cost):
                # (order.cost) is instantly calling the cost attributes under Menu Class

                # Creating the coffee
                coffee_bot.make_coffee(order)