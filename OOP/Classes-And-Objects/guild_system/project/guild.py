from player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):

        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        else:
            try:
                member = next(filter(lambda p: p.name == player.name, self.players))
                if member:
                    return f'Player {player.name} is already in the guild.'
            except StopIteration:
                return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):

        try:
            member = next(filter(lambda p: p.name == player_name, self.players))
            self.players.remove(member)
            member.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = f'Guild: {self.name}\n'
        for player in self.players:
            info += f'{player.player_info()}\n'

        return info


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
