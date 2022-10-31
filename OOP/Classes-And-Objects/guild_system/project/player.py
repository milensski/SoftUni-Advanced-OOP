class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        info = ''
        info += f'Name: {self.name}\n'
        info += f'Guild: {self.guild}\n'
        info += f'HP: {self.hp}\n'
        info += f'MP: {self.mp}\n'

        for skill, mana in self.skills.items():
            info += f'==={skill} - {mana}\n'

        return info

