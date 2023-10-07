import random
import string
def knight(p):
    p.attack(5)
    p.draw()

def healer(p):
    p.heal(5)
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
    print("useing function number"+str(index))
    functions[index](p)
    characters = string.ascii_letters + string.digits + string.punctuation
    newSpell = ''.join(random.choice(characters) for _ in range(6))
    newSpell = newSpell.replace(" ","")
    spells[names.index("Autotainment")] = newSpell



names = ["Knight","Healer", "Crimson Demon", "Crabulord","Crab Nest", "Crab","Autotainment"]
functions = [knight, healer, explosion, crabLord, crabNest,crab, randCard]

effects = ["DMG: 5","Heal: 5 HP", "DMG: 99\ncreates the perfect\nexplosion",
"sacrifices all crab cards\nin your deck, dealing 5\ndamage each\nadd a crab to your deck","adds 2 crab cards to your\ndeck", 
"DMG: 2\nadds a crab to your deck\n -It's turing complete!","activates a random card\n -randomly generated"
]
spells = ["pow!", 
"restore", 
"""Summon before me the root
of thy power hidden
within the lands of the
kingdom of demise!
EEEXPLOSION!!!""",
"the crab lord cometh",
"clickity",
"clack",
""
]

characters = string.ascii_letters + string.digits + string.punctuation
newSpell = ''.join(random.choice(characters) for _ in range(6))
newSpell = newSpell.replace(" ","")
spells[names.index("Autotainment")] = newSpell





