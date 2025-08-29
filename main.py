from CoffeeMaker import MoneyMachine, CoffeeMaker, Menu, MenuItem

money_machine: MoneyMachine = MoneyMachine()
coffee_maker: CoffeeMaker = CoffeeMaker()
menu: Menu = Menu()

is_on: bool = True

while is_on:
    options: str = menu.get_items()
    choice: str = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink: MenuItem = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
                drink.cost
        ):
            coffee_maker.make_coffee(drink)
