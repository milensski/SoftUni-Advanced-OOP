from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }

    BOOTH_TYPES = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy, name, price):

        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = ChristmasPastryShopApp.DELICACY_TYPES[type_delicacy](name, price)

        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = ChristmasPastryShopApp.BOOTH_TYPES[type_booth](booth_number, capacity)

        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):

        try:
            booth = next(filter(lambda b: b.is_reserved is False and b.capacity >= number_of_people, self.booths))

        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth.booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number):

        booth = list(filter(lambda b: b.booth_number == booth_number, self.booths))[0]

        bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])

        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" + f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
