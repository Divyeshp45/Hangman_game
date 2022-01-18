

import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words=["applause","make","take"]
choosen_word=random.choice(words)
choosen_word1=len(choosen_word)
print(choosen_word)
user=[]
for num in range(choosen_word1):
    user+='_'
print(user)
lives=6
end_of_game=False
while not end_of_game:
    guess=input("ENTER A ALPHABET:\n").lower()
    for n in range(choosen_word1):
        letter=choosen_word[n]
        if letter==guess:
            user[n]=guess
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lost")

    if '_' not in user:
        end_of_game=True   
        print(user)
        print("you won")
    
    print(stages[lives])