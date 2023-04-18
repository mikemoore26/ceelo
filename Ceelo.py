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

    def shoot(self):
        text = f"{self.current_player.name} you rolled "

        curr_nums = []
        for die in self.dice.values():
            curr_nums.append(die.roll())
            text += f' {die.current_face} '

        text += '\n'
        print(text)

        return curr_nums

    def play(self):

        isShooting = True
        while isShooting:
            curr_nums = self.shoot()
            res = self.result(curr_nums, self.current_player.name)
            print(res)

            if res == "WON" or res == "LOST":
                isShooting = False


    def result(self, res, name):

        if 1 in res and 2 in res and 3 in res: # INSTANT LOST LOSS
            print(f"{name}  LOST")
            return 'LOST'

        if 4 in res and 5 in res and 6 in res: # INSTANT WIN
            print(f"{name}  WON")

            return "WON"

        if res[0] == res[1] == res[2]:
            print(f"{name}  Triple WON")
            return "WON"

        return None




if __name__ == '__main__':
    game = Celo(1)
    game.play()
