import battle
import shop
import cards
import random
from enemy import Enemy
from player import Player

def start():
    print(" ─══ THAT TIME I REINCARNATED A BUNCH OF HEROES INTO A TYPING GAME ══─ \n\nWhat do you want to name this world?")
    valid = False
    while not valid:
        name = input("")
        if len(name)>25:
            print("Too long. The name needs to be less than 25 characters")
        else:
            valid = True
    print("\n\n\nWelcome to "+name+""". The Demon King has risen once again, 
and you must summon legendary heros to save it. Unfortunately they're 
so weak they won't be able to do more than one thing before they're slain.
death is the first step to reincarnation though, so just summon them back
and everything will be fine! \n\n -ENTER TO CONTINUE""")
    input()  
    #print("\n\n\n\n\n\n\n\n "+"─"*80)
    print("\n\n\n\n\n\n  "+"─"*40+"─══ How To Play ══─"+"─"*40+"""
    - You will have 3 hero canidates in your hand, type out the special incantation (case sensitive) 
      on their card to summon them to the world of """+name+"""
    - When you summon a hero they will only be able to attack/do an action once before they are killed
    - The enemy will continuously destroy the world reducing its HP, even while you are in the middle 
      of summoning a hero. Summon heros to kill the enemy before it destroys the world.
    - Kill the Demon King's 6 evil minions in order to face the Demon King himself and save """+name)
    print(" "+"─"*100)
    print("""what types of heros are you looking for?
        
1) Basic Bunch:
    - very average heros, with average stats
    - good for learning the game
2) Defence Dudes
    - shield based cards
    - normal health
3) Crab Commander:
    - lots of crabs
    - more health
    - did you know crabs are turing complete
4) Chaotic Conjurer:
    - embrace the randomness
    - random health and heros
5) Hard Mode
    - small hand size
    - less health""")

    validInput = False
    timer = False
    while not validInput:
        print("enter the name or number of the group you want to select")

        text = input()
        if text.lower()=="1" or text.lower()=="Basic Bunch".lower():
            player = Player(name,[1,2,16],50)
            validInput = True
        elif text.lower()=="2" or text.lower()=="Defence Dudes".lower():
            player = Player(name,[4,5,6],50)
            validInput = True
        elif text.lower()=="3" or text.lower()=="Crab Commander".lower():
            player = Player(name,[8,8,10,11],60)
            validInput = True

        elif text.lower()=="4" or text.lower()=="Chaotic Conjurer".lower():
            deck = [12,13]
            for i in range(random.randrange(0,4)):
                deck.append(random.randrange(0,len(cards.names)))
            player = Player(name,deck,random.randrange(30,100))
            validInput = True
        elif text.lower()=="5" or text.lower()=="Hard Mode".lower():
            player = Player(name,[1,17,1],35)
            player.handSize = 2
            validInput = True
        elif text=="test":
            player = Player(name,[i for i in range(len(cards.names)-2)],100)
            validInput = True
        elif text.lower() =="speedrun":
            timer = True
            print("speedrun timer activated (starts when you select a group)")
        
          
    #shop.openShop(player)
    if timer:
        battle.makeBattle(player, Enemy(1), 0.0)
    else:
        #shop.openShop(player,0,-1)
        battle.makeBattle(player, Enemy(1), -1)

