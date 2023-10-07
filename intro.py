import battle
import shop
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
everything is destroyed.      == enter to start ==""")

    input()
    player = Player(name,[1,6,0])
    #shop.openShop(player)
    battle.makeBattle(player, Enemy(-1))

