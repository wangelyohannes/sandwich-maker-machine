import data
import sandwich_maker
import cashier


resources = data.resources
recipes = data.recipes

maker = sandwich_maker.SandwichMaker(resources)
pay_station = cashier.Cashier()

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        break

    if choice == "report":
        print(f"Bread: {maker.machine_resources['bread']} slice(s)\n")
        print(f"Ham: {maker.machine_resources['ham']} slice(s)")
        print(f"Cheese: {maker.machine_resources['cheese']} pound(s)")
        continue

    if choice in recipes:
        order = recipes[choice]
        if maker.check_resources(order["ingredients"]):
            coins = pay_station.process_coins()
            if pay_station.transaction_result(coins, order["cost"]):
                maker.make_sandwich(choice, order["ingredients"])
