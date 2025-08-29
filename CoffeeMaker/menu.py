class MenuItem:

    def __init__(
            self, name: str, water: int, milk: int, coffee: int, cost: float
    ) -> None:
        self.name: str = name
        self.cost: float = cost
        self.ingredients: dict[str, int] = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    def __init__(self) -> None:
        """
        Models the Menu with drinks.

        This class represents the menu containing multiple menu items.
        """
        self.menu: list[MenuItem] = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self) -> str:
        """
        Returns all the names of the available menu items.

        This method returns a string containing the names of all available menu items, separated by slashes.

        :Example:
        menu.get_items()
        "latte/espresso/cappuccino/"

        :return: A string of menu item names separated by slashes.
        :rtype: str
        """
        options: str = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name: str) -> MenuItem | None:
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None
