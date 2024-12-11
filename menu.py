from abc import ABC, abstractmethod
from typing import Dict, List


class MenuComponent(ABC):   # interface
    @abstractmethod
    def info(self, indent=0):
        pass

    @abstractmethod
    def price(self):
        pass


class Dishes(MenuComponent):  # Dishes
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def info(self, indent=0):
        print('-'*indent + f'Название: {self.name}, цена: {self.price}')

    def price(self):
        return self.price


class Menu(MenuComponent):  # menu
    def __init__(self, name):
        self.name = name
        self._munu = []

    def add(self, component):
        if not any(isinstance(x, Dishes) and x.name == component.name for x in self._munu):
            self._munu.append(component)

    def remove_(self, component):
        self._munu = [x for x in self._munu if x != component]

    def price(self) -> float:
        price = 0
        for component in self._munu:
            if isinstance(component, Menu):
                price += component.price()
            else:
                price += component.price
        return price

    def info(self, indent=0):
        print('-' * indent + f'Название: {self.name}')
        for component in self._munu:
            component.info(indent+4)

# client code


def main(name_of_menu: str, name_of_dishes: Dict[str, float], name_of_submenu: Dict[str, Dict[str, int]]):
    if not isinstance(name_of_menu, str) or not isinstance(name_of_dishes, dict) or not isinstance(name_of_submenu, dict):
        raise ValueError("Неправильный тип аргументов")

    menu = Menu(name_of_menu)
    for key, value in name_of_dishes.items():
        dishes = Dishes(key, value)
        menu.add(dishes)

    for key, value in name_of_submenu.items():
        submenu = Menu(key)
        for name, price in value.items():
            dishes = Dishes(name, price)
            submenu.add(dishes)
        menu.add(submenu)

    menu.info()


if __name__ == '__main__':
    name_of_menu = 'Our menu'
    name_of_dishes = {
        "Пицца Маргарита": 250,
        "Суши Ролл": 180,
        "Борщ": 120,
        "Салат Цезарь": 200,
        "Котлета по-Киевски": 300,
        "Пельмени": 150,
        "Шашлык": 280,
        "Плов": 220
    }
    name_of_submenu = {
        "Салаты": {
            "Цезарь": 200,
            "Греческий": 180,
            "Оливье": 220
        }
    }

    main(name_of_menu, name_of_dishes, name_of_submenu)













