import cards

def finishGame(player):
    heroes = []
    for card in player.deck:
        heroes.append(cards.names[card])
    print("you failed to destroy the demon king, and the world has been destroyed")
    print("your heros were:"+str(heroes))
    
