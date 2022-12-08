class Client:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.shopping_cart_quantity = {}
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):

        if len(value) == 10 and value.isdigit() and value[0] != 0:
            self.__phone_number = value

        else:
            raise ValueError("Invalid phone number!")




