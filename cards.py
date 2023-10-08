import random
import string
def protagonist(p):
    cards = len(set(p.deck))
    print(str(cards)+" unique cards")
    p.attack(cards*5)
    p.draw()

def knight(p):
    p.attack(5)
    p.draw()

def healer(p):
    p.heal(5)
    p.draw()

def defender(p):
    p.shield+=12
    p.draw()

def barbarian(p):
    print("dealing "+str(p.shield))
    p.attack(p.shield)
    p.shield = 0
    p.draw()

def explosion(p):
    p.attack(99)
    p.draw()
    
def crabLord(p):
    crabs = 0
    index = 0
    for card in p.deck:
        if names[card]=="Crab":
            index=card
            crabs+=1
    for i in range(crabs):
        p.removeFromDeck(index)

    p.attack(crabs*5)
    p.draw()
    p.addToDeck(names.index("Crab"))
def crablass(p):
    crabs = 0
    for card in p.hand:
        if names[card]=="Crab":
            crabs+=1
    p.attack(crabs*10)
    p.draw()

def crabNest(p):
    p.addToDeck(names.index("Crab"))
    p.addToDeck(names.index("Crab"))
    p.draw()

def crab(p):
    p.attack(2)
    p.deck.append(names.index("Crab"))
    p.draw()

def randCard(p):
    index = random.randrange(0,len(functions))
    print("using function number"+str(index))
    functions[index](p)
    characters = string.ascii_letters + string.digits + string.punctuation
    spells[names.index("Autotainment")] = randName(6)

def handShuffle(p):
    p.draw()
    for i in range(len(p.hand)):
        p.hand[i] = random.randrange(0,len(names))
    spells[names.index("Shuffle")] = randName(5)
    return False
    
    

def bigHand(p):
    p.handSize+=1
    p.removeFromDeck(names.index("Big Hands"))
    p.draw()
    p.draw()
    return True


def randName(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    newSpell = ''.join(random.choice(characters) for _ in range(length))
    newSpell = newSpell.replace(" ","")
    return newSpell
    
        



names = ["Protagonist","Knight","Healer", "Defender","Barbarian", "Crimson Demon","Crabulass", "Crabulord","Crab Nest", "Crab","Autotainment",
         "Shuffle", "Big Hands"]
functions = [protagonist,knight, healer,defender,barbarian, explosion, crablass, crabLord, crabNest,crab, randCard,handShuffle, 
             bigHand]

effects = ["Deals 5 damage per unique\ncard in your deck\n -The power of friendship","DMG: 5","Heal: 5 HP","gives 12 shield",
"Deals damage = shield\nRemoves all shield", "DMG: 99\nCreates the perfect\nexplosion",
"Deals 10 damage per crab\nin your hand",
"Sacrifices all crab cards\nin your deck, dealing 5\ndamage each\nAdds a crab to your deck","Adds 2 crab cards to your\ndeck\n -crabs for the crab god", 
"DMG: 2\nAdds a crab to your deck\n -It's turing complete!","Activates a random card\n -Randomly generated",
"Turns your hand into\nrandom cards", "Increases hand size by 1\nCard is removed from deck\nafteruse"
]
spells = ["so this is the Demon\nKing's power","hiya", 
"restore", "protection","charge!",
"""Summon before me the root
of thy power hidden
within the lands of the
kingdom of demise!
EEEXPLOSION!!!""",
"clackette",
"the crab lord cometh",
"clickity",
"clack",
randName(6),
randName(5),
"bigHandMode"
]







