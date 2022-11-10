from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.mro()[0].__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return f'Not enough budget'
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.mro()[0].__name__} hired successfully'
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= sum_of_salaries:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_costs = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= sum_of_costs:
            self.__budget -= sum_of_costs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        else:
            return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self):
        info = [f'You have {len(self.animals)} animals']
        info_dict = {'Lions': [],
                     'Tigers': [],
                     'Cheetahs': []
                     }
        for animal in self.animals:
            if type(animal).__name__ == 'Lion':
                info_dict['Lions'].append(animal)
            elif type(animal).__name__ == 'Tiger':
                info_dict['Tigers'].append(animal)
            elif type(animal).__name__ == 'Cheetah':
                info_dict['Cheetahs'].append(animal)

        info.append(f'----- {len(info_dict["Lions"])} Lions:')
        for lion in info_dict['Lions']:
            info.append(lion.__repr__())
        info.append(f'----- {len(info_dict["Tigers"])} Tigers:')
        for tiger in info_dict['Tigers']:
            info.append(tiger.__repr__())
        info.append(f'----- {len(info_dict["Cheetahs"])} Cheetahs:')
        for cheetah in info_dict['Cheetahs']:
            info.append(cheetah.__repr__())

        return '\n'.join(info)

    def workers_status(self):
        info = [f'You have {len(self.workers)} workers']
        info_dict = {'Keepers': [],
                     'Caretakers': [],
                     'Vets': []
                     }
        for worker in self.workers:
            if type(worker).__name__ == 'Keeper':
                info_dict['Keepers'].append(worker)
            elif type(worker).__name__ == 'Caretaker':
                info_dict['Caretakers'].append(worker)
            elif type(worker).__name__ == 'Vet':
                info_dict['Vets'].append(worker)

        info.append(f'----- {len(info_dict["Keepers"])} Keepers:')
        for keeper in info_dict['Keepers']:
            info.append(keeper.__repr__())
        info.append(f'----- {len(info_dict["Caretakers"])} Caretakers:')
        for caretaker in info_dict['Caretakers']:
            info.append(caretaker.__repr__())
        info.append(f'----- {len(info_dict["Vets"])} Vets:')
        for vet in info_dict['Vets']:
            info.append(vet.__repr__())

        return '\n'.join(info)

