# Stand alone version of ex43's battle system study drill
# For Python 3

from random import randint
import os

class Character(object):
    
    def __init__(self, life = 3):
        self.life = life


class Combat(object):
    """
    1. Jag kör med klasser eftersom det är var jag är i boken.
    2. Jag använder sten sax påse som stridssystem.
    3. Motståndaren använder inte random utan den vetenskapligt
       framtagna metoden för att troligast vinna:
        1. Har man just vunnit en omgång är det troligare att man 
           kör samma val igen.
        2. Har man just förlorat är det troligare att man byter 
           (och då till det val som vinner över vad motståndaren
           använt denna omgång?)
    """
    
    def fight(self):
        self.hero = Character()
        self.gothon = Character()
        os.system('clear')
        print("Rock Paper Scissors")
        three_things = ["rock", "paper", "scissors"]
        goth_choice = three_things[randint(0, 2)]
        # print(goth_choice)
        print("your life:", self.hero.life)
        print("despicable monster's life:", self.gothon.life, "\n")
        
        while self.hero.life > 0 and self.gothon.life > 0:
            
            choice = input("> ").lower()
            
            if choice == goth_choice:
                os.system('clear')
                print("draw!")
                goth_choice = three_things[randint(0, 2)]
            elif choice == "rock" and goth_choice == "paper":
                self.combat_print(0, goth_choice)
                goth_choice = "rock"
            elif choice == "paper" and goth_choice == "scissors":
                self.combat_print(0, goth_choice)
                goth_choice = "paper"
            elif choice == "scissors" and goth_choice == "rock":
                self.combat_print(0, goth_choice)
                goth_choice = "scissors"
            elif choice == "rock" and goth_choice == "scissors":
                self.combat_print(1, goth_choice)
                goth_choice = "paper"
            elif choice == "paper" and goth_choice == "rock":
                self.combat_print(1, goth_choice)
                goth_choice = "scissors"
            elif choice == "scissors" and goth_choice == "paper":
                self.combat_print(1, goth_choice)
                goth_choice = "rock"
            else:
                os.system('clear')
                print("Choose between rock, paper and scissors.")
                
            
            
            print("\nyour life:", self.hero.life)
            print("despicable monster's life:", self.gothon.life, "\n")

    
    def combat_print(self, n, g_choice):
        os.system('clear')
        
        if n == 0:
            print("Gothon choose", g_choice)
            print("you lose!")
            self.hero.life -= 1
        elif n == 1:
            print("Gothon choose", g_choice)
            print("you win!")
            self.gothon.life -= 1


play = Combat()
play.fight()
