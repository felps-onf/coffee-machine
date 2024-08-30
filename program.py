def run():
    resources = {
       "water": 2000,
       "milk": 1000,
       "coffee": 500,
       "money": 500,
    }
    
    coins_table = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    
    menu = {
        "espresso": {'recipe':{"water": 50, "coffee": 18, "milk": 0}, "price": 1.50},
        "latte": {'recipe':{"water": 200, "coffee": 24, "milk": 150}, "price": 2.50},
        "cappuccino": {'recipe':{"water": 250, "coffee": 24, "milk": 100}, "price": 3.0}
    }
    
    
    def check_resources(menu, resources, order):
        message = ""
        water_check = False
        milk_check = False
        coffee_check = False
        
        if resources['water'] >= menu[order]['recipe']['water']:
            water_check = True
        if resources['milk'] >= menu[order]['recipe']['milk']:
            milk_check = True
        if resources['coffee'] >= menu[order]['recipe']['coffee']:
            coffee_check = True
            
        if water_check and milk_check and coffee_check:
            return "ok"
        
        else:
            message = f"Sorry there is not enough "
            items = []
            if not water_check:
                items.append("water")
            if not milk_check:
                items.append("milk")
            if not coffee_check:
                items.append("coffee")
                
            if len(items) > 0:
                message += ", ".join(items)
                        
            return message
    
    def process_coins(quarters, dimes, nickel, pennies):
        total = 0
        if quarters > 0:
            total += coins_table['quarters'] * quarters
        if dimes > 0:
            total += coins_table['dimes'] * dimes
        if nickel > 0:
            total += coins_table['nickles'] * nickel
        if pennies > 0:
            total += coins_table['pennies'] * pennies
        return total
    
    
    def make_coffee(order):
        resources['water'] -= menu[order]['recipe']['water']
        resources["milk"] -= menu[order]['recipe']['milk']
        resources['coffee'] -= menu[order]['recipe']['coffee']
    
    
    def process_transaction(order, value):
        if menu[order]["price"] < value:
            aux_money = resources["money"]
            aux = value
            
            aux -= menu[order]["price"]
            
            aux_money += menu[order]["price"]
            aux_money -= aux


            if aux_money >= aux and aux > 0 and aux_money > 0:
                report_before = report(resources)
                print(f"Report before purchasing {user_order}:\n")
                print(report_before)        
                
                value -= menu[order]["price"]
                
                resources['money'] += menu[order]["price"]
                resources['money'] -= value
                print(f"Here is ${value:.2f} dollars in change.\n")
                return True
            else:
                print(f"There is not enough money for the charge!\n")
                return False
            
            
        elif menu[order]["price"] == value:
            report_before = report(resources)
            print(f"Report before purchasing {user_order}:\n")
            print(report_before)
            value -= menu[order]["price"]
            resources['money'] += menu[order]["price"]
            return True
        else:
            print(f"There is not enough money for purchase the coffee!\n")
            return False
    
    def report(resources):
        formated_message =  f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${float(resources['money'])}\n"
        return formated_message
    
    while True:
        print("--------------------------------------")
        print("Welcome!")
        print("options: ")
        print(f"-> order a coffee: espresso, latte or cappuccino")
        print(f"-> report: report")
        print(f"-> exit: off")
        print("--------------------------------------")

        user_order = input("What would you like? ")
        
        if user_order == "report":
            message = report(resources)
            print(message)
            
        
        
        elif user_order == "off":
            break
        
        elif user_order in ["espresso", "latte", "cappuccino"]:
            check_status = check_resources(menu, resources, user_order)
            if check_status == "ok":
                print("Insert your coins!")
                quarters = int(input("quarters: "))
                dimes = int(input("dimes: "))
                nickel = int(input("nickel: "))
                pennies = int(input("pennies: "))
                final_value = process_coins(quarters, dimes, nickel, pennies)
                print(f"Total value: {final_value}")
                transaction_checked = process_transaction(user_order, final_value)
                if transaction_checked:
                    make_coffee(user_order)
                    report_after = report(resources)
                    print(f"Report after purchasing {user_order}:\n")
                    print(report_after)
                    print(f"Here is you {user_order}. Enjoy!")
                    user_order = ""
        else:
            print(f"Insert a correct option!")
                
    

    
if __name__ == "__main__":
    run()