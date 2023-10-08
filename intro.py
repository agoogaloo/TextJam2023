import battle
import cards
import random
from enemy import Enemy
from player import Player

def start():
    print("What do you want to name this world?")
    name = input("")
    print("\n\n\nWelcome to "+name+""". The great demon king has risen once again, 
and you must summon legendary heros to save it. Unfortunately they're 
so weak they won't be able to more than one thing before they're slain.
death is the first step to reincarnation though, so just summon them back
and everything will be fine!
          
you can summon a hero candidate by typing their special incantation (case sensitive), 
but the demon king is already destroying the world, so summon them quickly, before 
everything is destroyed. 
          
what types of heros are you looking for?
        
1) Basic Bunch:
    - very average heros, with average stats
2) Crab Commander:
    - lots of crabs
    - low health
    - did you know crabs are turing complete
3) Chaotic Conjurer:
    - embrace the randomness
    - random stats and heros
          """)

    validInput = False
    while not validInput:
        text = input()
        if text.lower()=="1" or text.lower()=="Basic Bunch".lower():
            player = Player(name,[1,1,2,3],50)
            validInput = True

        elif text.lower()=="2" or text.lower()=="Crab Commander".lower():
            player = Player(name,[6,6,8,9],20)
            validInput = True

        elif text.lower()=="3" or text.lower()=="Chaotic Conjurer".lower():
            deck = [10,11]
            for i in range(random.randrange(0,4)):
                deck.append(random.randrange(0,len(cards.names)))
            player = Player(name,deck,random.randrange(30,90))
            
            validInput = True
        else:
            print("enter the name or number of the group you want to select")

    #shop.openShop(player)
    battle.makeBattle(player, Enemy(1))

