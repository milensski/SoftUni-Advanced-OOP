from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = []
        for meal in self.menu:
            result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.clients_list.append(Client(client_phone_number))

        current_client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        for meal_name, meal_quantity in meal_names_and_quantities.items():

            try:
                meal = next(filter(lambda m: m.name == meal_name, self.menu))

            except StopIteration:

                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu))

            current_client.shopping_cart.append(meal)
            current_client.bill += meal.price * meal_quantity
            meal.quantity -= meal_quantity
            current_client.shopping_cart_quantity[meal_name] = meal_quantity

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(map(str, current_client.shopping_cart))} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):

        current_client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(current_client.shopping_cart) > 0:
            for meal_name, meal_quantity in current_client.shopping_cart_quantity.items():
                for meal in self.menu:
                    if meal.name == meal_name:
                        meal.quantity += meal_quantity

            current_client.shopping_cart = []
            current_client.bill = 0.0
            current_client.shopping_cart_quantity = {}

        else:
            raise Exception("There are no ordered meals!")

        return f"Client {current_client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        current_client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(current_client.shopping_cart) > 0:

            current_client.shopping_cart = []
            bill = current_client.bill
            current_client.shopping_cart_quantity = {}

            current_client.bill = 0.0
            self.receipt_id += 1

            return f"Receipt #{self.receipt_id} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

        else:

            raise Exception("There are no ordered meals!")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
