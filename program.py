def run():
    resources = {
        "water": 2000,
        "milk": 1000,
        "coffee": 500,
        "money": 500,
    }

    coins_table = {
        "one_dollar": 1.0,
        "half_dollar": 0.5,
        "quarter_dollar": 0.25,
    }

    menu = {
        "espresso": {'recipe': {"water": 50, "coffee": 18, "milk": 0}, "price": 1.50},
        "latte": {'recipe': {"water": 200, "coffee": 24, "milk": 150}, "price": 2.50},
        "cappuccino": {'recipe': {"water": 250, "coffee": 24, "milk": 100}, "price": 3.0}
    }

    def check_resources(menu, resources, order):
        missing = [item for item in menu[order]['recipe'] if resources[item] < menu[order]['recipe'][item]]
        if not missing:
            return "ok"
        return f"Sorry, there is not enough " + ", ".join(missing)

    def show_menu():
        message = ""
        for key, value in menu.items():
            message += f"Coffee: {key} --- Price:  ${value['price']}\n"
        return message

    def process_coins(one_dollar, half_dollar, quarter_dollar):
        return (one_dollar * coins_table['one_dollar'] +
                half_dollar * coins_table['half_dollar'] +
                quarter_dollar * coins_table['quarter_dollar'])

    def make_coffee(order):
        for item in menu[order]['recipe']:
            resources[item] -= menu[order]['recipe'][item]

    def process_transaction(order, value):
        if value < menu[order]["price"]:
            print(f"Insufficient funds! The price of {order} is ${menu[order]['price']:.2f}.")
            return False

        change = value - menu[order]["price"]
        if change > resources['money']:
            print("Sorry, there is not enough money for the change!")
            return False

        resources['money'] += menu[order]["price"]
        if change > 0:
            resources['money'] -= change
            print(f"Here is ${change:.2f} in change.")
        return True

    def report():
        return (f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
                f"Coffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}\n")

    while True:
        print("--------------------------------------")
        print("Welcome!")
        print("Options: espresso, latte, cappuccino, report, menu, off")
        print("--------------------------------------")

        user_order = input("What would you like? ").strip().lower()

        if user_order == "menu":
            print(show_menu())
        elif user_order == "report":
            print(report())
        elif user_order == "off":
            print("Turning off the machine. Goodbye!")
            break
        elif user_order in menu:
            check_status = check_resources(menu, resources, user_order)
            if check_status == "ok":
                print("Please insert coins.")
                try:
                    one_dollar = int(input("One Dollar coins: "))
                    half_dollar = int(input("Half Dollar coins: "))
                    quarter_dollar = int(input("Quarter Dollar coins: "))
                except ValueError:
                    print("Invalid input! Please enter whole numbers for the coins.")
                    continue
                
                total_value = process_coins(one_dollar, half_dollar, quarter_dollar)
                print(f"Total inserted: ${total_value:.2f}")

                if process_transaction(user_order, total_value):
                    make_coffee(user_order)
                    print(f"Here is your {user_order}. Enjoy!")
                    print(report())
            else:
                print(check_status)
        else:
            print("Invalid option! Please choose from the menu.")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
