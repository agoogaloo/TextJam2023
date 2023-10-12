import intro
import shop
import cards

def winGame(player, level, time):
    print("\n\n\n\n\n\n\n"+"═"*85)
    print(player.name+" is finally safe from the Demon King, and only a few heros died in the process")
    if time!=-1:
         print("you won in "+str(time)+"seconds")
    print("─"*85)
    print(" HALL OF HEROES:")
    for card in player.deck:
            print(" -"+cards.names[card]+": "+cards.effects[card].replace("  ","").replace("\n", " "))
    print("─"*60)
    valid = False
    while not valid:
        print("--OPTIONS--")
        print(" - type 'contiue' to continue in endless mode")
        print(" - type 'reset' to restart the game")
        print(" - type 'quit' to exit")
        text = input()
        if text.lower() == "quit":
            valid = True
        elif text.lower() =="continue":
            shop.openShop(player, level, time)
        elif text.lower() == "reset":
            intro.start()
            valid = True