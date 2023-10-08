import cards
import intro

def finishGame(player, level):
    heroes = []
    for card in player.deck:
        heroes.append(cards.names[card])
    print("\n\n\n\n"+"═"*65)
    print(player.name+" has been destroyed by the demon king and all hope is lost :(")
    print("─"*65)
    print("your deck of candidates was:")
    for card in player.deck:
        print(" -"+cards.names[card])
        print("     -"+cards.effects[card].replace("  ","").replace("\n", " "))
    print("─"*65)
    print("you reached level "+str(level))
    print("─"*65)
    valid = False
    while not valid:
        text = input("\ntype 'quit' to exit or 'reset' to start again\n")
        if text.lower() == "quit":
            valid = True
        elif text.lower() == "reset":
            intro.start()
            valid = True
       
          
        
    
