class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, has_player):
        for player in self.players:
            if player == has_player:
                return True
        else:
            return False

    def play_game(self, outcome):
        if outcome == True:
            self.points = +3
