from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):

        if horse_name in [h.name for h in self.horses]:
            raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type in self.HORSE_TYPES:
            self.horses.append(self.HORSE_TYPES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f'Jockey {jockey_name} has been already added!')

        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):

        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))

        return f'Race {race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey = list(filter(lambda j: j.name == jockey_name, self.jockeys))[0]
        except IndexError:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        try:
            horse = list(filter(lambda h: h.is_taken is False and h.__class__.__name__ == horse_type, self.horses))[-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey.name} already has a horse."

        horse.is_taken = True

        jockey.horse = horse

        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))

        except StopIteration:

            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:

            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f'Jockey {jockey.name} has been already added to the {race.race_type} race.'

        race.jockeys.append(jockey)

        return f"Jockey {jockey.name} added to the {race.race_type} race."

    def start_horse_race(self, race_type: str):

        try:

            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race.race_type} needs at least two participants!")


        winner = max(race.jockeys, key=lambda j: j.horse.speed)

        return f"The winner of the {race.race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
