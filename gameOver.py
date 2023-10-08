import cards

def finishGame(player, level):
    heroes = []
    for card in player.deck:
        heroes.append(cards.names[card])
    print("\n\n\n\n\you failed to destroy the demon king, and the world has been destroyed")
    print("your heros were:"+str(heroes))
    print("you reached level "+str(level))
    
