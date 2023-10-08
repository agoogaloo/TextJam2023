import intro
import shop
import cards

def winGame(player, level):
    print("\n\n\n\n"+"═"*90)
    print(player.name+" is finally safe from the Demon King, and only a few heros died in the process")
    print("─"*65)
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
            shop.openShop(player, level)
        elif text.lower() == "reset":
            intro.start()
            valid = True