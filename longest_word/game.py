# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import requests
import random

def is_dict(word):
    url = "https://wagon-dictionary.herokuapp.com/"
    response = requests.get(url + word)
    data = response.json()
    return data["found"]

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = None
        letter_list = []
        for i in range(1,10):
            rd_letter = random.choice(string.ascii_uppercase)
            letter_list.append(rd_letter)
        self.grid = letter_list

    def is_valid(self, word):
        if not word:
            return False
        if not is_dict(word):
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True


game = Game()
print(game.grid) # --> OQUWRBAZE
my_word = "BAROQUE"
game.is_valid(my_word) # --> True
