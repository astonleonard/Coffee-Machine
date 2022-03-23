# Todo: 2. Check resources sufficient to make drink order.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Todo: 1. Print report of all coffee machine resources


def coins():
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01
    result = quarters + dimes + nickles + pennies
    return result


def coffee_machine():
    off = False
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = 0
    while not off:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")

        elif choice == 'off':
            off = True

        else:
            cost = MENU[choice]['cost']
            new_coffee_resources = MENU[choice]['ingredients']['coffee']
            new_water_resources = MENU[choice]['ingredients']['water']
            coffee = coffee - new_coffee_resources
            water = water - new_water_resources

            result = coins()
            if result < cost:
                print("Sorry that's not enough money")
            elif result > cost:
                a = result - cost
                if choice == 'latte' or choice == 'cappuccino':
                    new_milk_resources = MENU[choice]['ingredients']['milk']
                    milk = milk - new_milk_resources
                    if milk <= -1:
                        milk += new_milk_resources
                        print("Sorry there is not enough milk.")

                if coffee <= -1 or water <= -1:
                    if coffee <= -1:
                        coffee += new_coffee_resources
                        print("Sorry there is not enough coffee.")

                    if water <= -1:
                        water += new_water_resources
                        print("Sorry there is not enough water.")

                else:
                    print(f"Here is ${a:.2f} dollars in change.")
                    money += cost
                    print(f"Here is your {choice}. Enjoy!")


coffee_machine()
