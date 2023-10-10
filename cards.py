import random
import string
def protagonist(p):
    cards = len(set(p.deck))
    print(str(cards)+" unique cards")
    p.attack(cards*5)
    p.draw()

def knight(p):
    p.attack(8)
    p.draw()

def healer(p):
    p.heal(5)
    p.draw()

def defender(p):
    p.shield*=2
    p.draw()

def barbarian(p):
    print("dealing "+str(p.shield))
    p.attack(p.shield)
    p.shield = 0
    p.draw()

def druid(p):
    p.shield+=int(1.5*len(spells[names.index("Druid")]))
    p.draw()
def allOutAttack(p):
    
    oneShotUsed = False
    for i in range(len(p.hand)-1,-1,-1):
        print("indexe "+str(i))
        #stopping it from using itself
        if functions[p.hand[i]]==allOutAttack:
            p.hand.pop(i)
            p.draw()
            print("skipping self")
            cardSkipped = True
            continue
        card = p.hand[i]
        print("using "+names[card])
        if (not (oneShotUsed and functions[p.hand[i]]==bigHand)) and p.useCard(i):
            oneShotUsed = True
            print("used a bighands")

        if oneShotUsed:
            for j in range(p.hand.count(names.index("Big Hands"))):
                p.hand.remove(names.index("Big Hands"))
                p.draw()

    p.draw()
    return True
            

        


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
def crabCoat(p):
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

def stun(p):
    p.stun(1.5)
    p.draw()

def quickAttack(p):
    p.attack(3)
    p.draw()

def randName(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    newSpell = ''.join(random.choice(characters) for _ in range(length))
    newSpell = newSpell.replace(" ","")
    return newSpell


    


names = ["Protagonist","Knight","Healer","Phantom Theif", "Defender","Barbarian","Druid", "Crimson Demon","Crabs in a Trench Coat", 
         "Crabulord","Crab Nest", "Crab","Autotainment","Shuffle", "Big Hands", "Ice Wizard","Rogue"]
functions = [protagonist,knight, healer,allOutAttack,defender,barbarian,druid, explosion, crabCoat, crabLord, crabNest,crab, 
             randCard,handShuffle, bigHand,stun,quickAttack]

effects = ["Deals 5 damage per unique\ncard in your deck\n-The power of friendship","DMG: 8","Heal: 5 HP",
"Uses all of the cards\nin your hand","doubles current shield",
"Deals damage = shield\nRemoves all shield",
"gives shield proportional\nto the world names length\nshouldnt see this",
"DMG: 99\nCreates the perfect\nexplosion",
"Deals 10 damage per crab\nin your hand\n",
"Sacrifices all crab cards\nin your deck, dealing 5\ndamage each\nAdds a crab to your deck",
"Adds 2 crab cards to your\ndeck\n -Crabs for the crab god", 
"DMG: 2\nAdds a crab to your deck\n -your hand evolves\n  into crabs",
"Activates a random card\n-Randomly generated",
"Turns your hand into\nrandom cards",
"Increases hand size by 1\nCard is removed from deck\nafteruse",
"Freezes enemy for 1.5\nseconds\n -lost his super suit","DMG: 3"
]
spells = ["so this is the Demon\nKing's power","Kapow!", 
"restore","time for an all out\nattack", "protection","charge!","shouldnt see this",
"""Summon before me the root
of thy power hidden
within the lands of the
kingdom of demise!
EEEXPLOSION!!!""",
"click click",
"the crab lord cometh",
"clickity",
"clack",
randName(6),
randName(5),
"bigHandMode",
"ice ice baby","ha"
]

def setWorldName(name):
    spells[names.index("Druid")]=name
    effects[names.index("Druid")] = "Adds "+str(int(1.5*len(spells[names.index("Druid")])))+" shield"



