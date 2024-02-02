# class Roulette

import random

class Roulette:
    def __init__(self):
        self.numbers = list(range(1, 11))
        self.drawn_numbers = []

    def spin(self):
        if len(self.drawn_numbers) < 10:
            result = random.choice(self.numbers)
            self.drawn_numbers.append(result)
            return result
        else:
            result = "Jackpot"
            print("Congratulations! Jackpot!")
            return result
