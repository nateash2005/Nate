import string
import random
import nltk
nltk.download('words')
from nltk.corpus import words
word_base = words.words()
acceptable = [i.lower() for i in word_base if 5<= len(i) <= 12]
LIVES = 8
LETTERS = string.ascii_lowercase
HANGMAN = [
    """
        +---+
            |
            | 
            |
            |
           /|
          / |
===================""",
    """
        +---+
        |   |
            | 
            |
            |
           /|
          / |
===================""",
    """
        +---+
        |   |
        0   | 
            |
            |
           /|
          / |
==================""",
  """
        +---+
        |   |
        0   | 
        |   |
            |
           /|
          / |
==================""",
 """
        +---+
        |   |
        0   | 
       /|   |
            |
           /|
          / |
==================""",
"""
        +---+
        |   |
        0   | 
       /|\  |
            |
           /|
          / |
==================""",
"""
        +---+
        |   |
        0   | 
       /|\  |
       /    |
           /|
          / |
==================""",

"""
        +---+
        |   |
        0   | 
       /|\  |
       / \  |
           /|
          / |
==================  
GAME OVER
"""]

class Hangman_Game:
    def __init__(self,acceptable):
        self.word = random.choice(acceptable)
        self.guessed = set()
        self.lives = LIVES
        self.hidden_word = ["_"] * len(self.word)
     
    def guess_sorter(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if guess in LETTERS and len(guess) == 1:
                return guess
            print("Invalid letter. Try again")
       
    def make_guess(self,guess):
        if guess in self.guessed:
            print(f"You have already guessed {guess}. Try again.")
            return False
    
        self.guessed.add(guess)
        
        if guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.hidden_word[index] = guess
            return True
        else:
            self.lives -=1
            return False
        
    def is_won(self):
        return "_" not in self.hidden_word
    
    def is_lost(self):
        return self.lives  == 1
    
    def play(self):
        while not self.is_won() and not self.is_lost():
          
            print("Guessed letters:", " ".join(sorted(self.guessed)))
            guess = self.guess_sorter()
            self.make_guess(guess)
            print(HANGMAN[LIVES - self.lives])
            print(" ".join(self.hidden_word))
            
            
        if self.is_won():
            print("Congratulations! The word was:", " ".join(self.word))
            return True
        if self.is_lost():
            print("Unlucky! The word was: ", " ".join(self.word))
            
            return False
            
    
            

if __name__ == "__main__": 
    game = Hangman_Game(acceptable)
    game.play()
        


