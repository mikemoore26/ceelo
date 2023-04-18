# pylint:disable=E0001
from Dice import *
from Player import Player


class Celo():
    def __init__(self, num):
        self.dice = {}
        self.num_players = num
        self.current_player_i = 0
        self.current_player = None
        self.players = []
        self.inProgress = False
        self.init()

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)

    def next_turn(self):
        self.current_player_i += 1
        if self.current_player_i == len(self.players):
            self.current_player_i = 0

        self.current_player = self.players[self.current_player_i]

    def init(self):
        self.get_dice()
        self.players = []
        for _ in range(self.num_players):
            self.add_player(Player(input("Name?")))

        self.current_player = self.players[0]

    def get_dice(self):
        self.dice = {}
        for i in range(3):
            self.dice[i] = Dice()

    def play(self):
        text = f"{self.current_player.name} you rolled "
        curr_nums = []
        for die in self.dice.values():
            curr_nums.append(die.roll())
            text += f' {die.current_face} '


        print(curr_nums)
        text += '\n'
        print(text)

    def result(self, res):
        res = []
        if res.


if __name__ == '__main__':
    game = Celo(1)
    game.play()
