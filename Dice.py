import random


class Dice():
    def __init__(self):
        self.faces = [x for x in range(7)]
        self.current_face = None
        self.history = []

    def roll(self, num=1):
        # for _ in range(num):
        self.current_face = random.choice(self.faces)

        print(f'you rolled an {self.current_face}')
        self.history.append(self.current_face)
        return self.current_face

    def print_history(self):
        text = "***** HISTORY *****\n"
        for i, num in enumerate(self.history):
            text += f'{i + 1} : {num}\n'

        return text


if __name__ == '__main__':
    dice = Dice()

    for _ in range(5):
        dice.roll()

    print(dice.print_history())


