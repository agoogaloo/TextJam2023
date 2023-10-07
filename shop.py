import random
import cards
import battle
from enemy import Enemy


cardWidth = 27
border = " "+(("═"*cardWidth)+" ")*3
incantationHeader = "║"+((" "*7)+"-INCANTATION-"+" "*7+"║")*3
splitBorder = "║"+(("-"*cardWidth)+"║")*3

def openShop(player):
    finished = False
    options = createOptions()
    while not finished:
        print("\n\n\n\n\n"+border)
        print("   -welcome to the shop-")
        print(" here you can find heros you will be able to summon later")
        print(border)
        
        #printing the current deck
        print("your currently selected candidates are:")    
        for card in player.deck:
            print(" -"+cards.names[card]+": "+cards.effects[card].replace("\n", " "))
        print(player.name+" has "+str(player.health)+"/"+str(player.maxHealth)+" HP")
        printCards(options)
       
        print("\n--CHOOSE AN OPTION--")
        print(" - type 'add <hero name> to add a candidate to your deck")
        print(" - type 'heal' to restore the world to max health")
        print(" - type 'health up' to increase max health by 10")
        print(" - type 'remove <hero name>' to remove a candidate from your deck")    

   
        text = input()
        finished = selectOption(text, player, options)
    player.hand = []
    battle.makeBattle(player, Enemy())
            

def selectOption(text, player,options):
    if text.lower()=="heal":
        print("healing")
        player.health = player.maxHealth
        return True
    elif text.lower()=="health up":
        print("HP++")
        player.maxHealth+=10
        return True
        
    elif text.lower().find("remove ")!=-1:
        text = text.replace("remove ", "")
        success = False
        for card in player.deck:
            if cards.names[card].lower()==text.lower():
                print("removing card")
                player.deck.remove(card)
                return True
        if not success:
            print("coundt find a "+text+" card in your deck")
            
    elif text.lower().find("add ")!=-1:
        text = text.replace("add ", "")
        #text = text.replace(" ", "")
        for card in options:
             print("adding card")
             if cards.names[card].lower()==text.lower:
                  player.deck.append(card)
                  return True
    return False
         

def createOptions():
    options = []
    for i in range(3):
        options.append(random.randrange(0,len(cards.names)))
    return options

def printCards(hand):
    #creating the names of the cards
    names = "║"
    for card in hand:
        nameSize = len(cards.names[card])
        spaceUsed =int((cardWidth-nameSize)/2)
        names+=" "*(spaceUsed)
        names+=cards.names[card]
        spaceUsed+=nameSize
        names+=" "*(cardWidth-spaceUsed)
        names+="║" 

    #creating effects row

    effects = []
    effectLines = []
    for effect in cards.effects:
            effectLines.append(effect.split("\n"))
    finishedText = False
    lineIndex = 0
    while not finishedText:
        line = "║"
        finishedText= True
        for card in hand:
            effectLine = effectLines[card]
            if lineIndex>=len(effectLine):
                line+=" "*cardWidth+"║"
                continue
            line+=effectLine[lineIndex]
            line+=" "*(cardWidth-len(effectLine[lineIndex]))+"║"
            finishedText = False
        if not finishedText:
            effects.append(line)
        lineIndex+=1

    #creating incantation row
    
    spells = []
    spellLines = []
    for spell in cards.spells:
            spellLines.append(spell.split("\n"))
    finishedText = False
    lineIndex = 0
    while not finishedText:
        line = "║"
        finishedText= True
        for card in hand:
            spellLine = spellLines[card]
            if lineIndex>=len(spellLine):
                line+=" "*cardWidth+"║"
                continue
            line+=spellLine[lineIndex]
            line+=" "*(cardWidth-len(spellLine[lineIndex]))+"║"
            finishedText = False
        if not finishedText:
            spells.append(line)
        lineIndex+=1
        
    #adding all the lines into one array (creating the actual menu)
    lines = [border,names,splitBorder]
    for line in effects:
            lines.append(line)
    lines.append(splitBorder)
    lines.append(incantationHeader)
    lines.append(splitBorder)
    for line in spells:
            lines.append(line)
    lines.append(border)
    for line in lines:
        print(line)