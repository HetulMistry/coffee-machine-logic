from .coffee_maker import CoffeeMaker
from .menu import Menu, MenuItem
from .money_machine import MoneyMachine

__all__ = ["CoffeeMaker", "Menu", "MenuItem", "MoneyMachine"]

__version__ = "1.0.0"
__author__ = "Hetul Mistry"

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# logger.info("CoffeeMaker package initialized")


def __repr__():

    return (
        f"CoffeeMaker Package: Version {__version__}, "
        f"Author {__author__}, "
        "Classes available - CoffeeMaker, Menu, MenuItem, MoneyMachine"
    )
