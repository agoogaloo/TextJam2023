import random
import cards
import battle
import time
from enemy import Enemy


cardWidth = 27
border = " "+(("═"*cardWidth)+" ")*3
incantationHeader = "║"+((" "*7)+"-INCANTATION-"+" "*7+"║")*3
splitBorder = "║"+(("-"*cardWidth)+"║")*3

tips = ["If you have multiple of the same hero in your hand, you can summon all of them at once!",
        "Enemies will wait for you to do something before they start attacking. What a gentleman",
        "Salsa goes really well with grilled cheese. Try it out sometime!",
        "Making your deck bigger doesn't always mean it's better.",
        "Enemies don't stop attacking, even while you're summoning a hero. Don't stop typing!",
        "just because you only have 1 of a card in your deck, doesn't mean you can't have more than 1 in your hand",
        "Theres no limit to your shield, but it resets every battle",
        "Your shield will block any damage that would normally go to your health",
        "Type 'speedrun' when selecting a team to show the speedrun timer"]

def openShop(player, level, timer):
    finished = False
    options = createOptions()
    startTime = time.time()
    while not finished:
        #options = createOptions()
        print("\n\n\n\n\n"+border)
        print("   -WELCOME TO THE SHOP-")
        if timer!=-1:
            print("TIME: {:.3f} sec.".format(timer+time.time()-startTime))
        print("TIP: "+tips[random.randrange(0,len(tips))])
        print(border)
        
        #printing the current deck
        print("your current deck of candidates is:")    
        for i in range(len(player.deck)):
            card = player.deck[i]
            print("- " + str(i)+". "+cards.names[card]+": "+cards.effects[card].replace("  ","").replace("\n", " "))
        print("─"*35)
        line = player.name+" HP: "+str(player.health)+"/"+str(player.maxHealth)
        print(line+" "*(35-len(line))+"|")
        printCards(options)
       
        print("\n--CHOOSE AN OPTION--")
        print(" - type 'add <card number/hero name> to add a candidate to your deck and heal to max hp")
        print(" - type 'health up' to increase max health by "+str(15))
        if len(player.deck)>3:
            print(" - type 'remove <card number/hero name>' to remove a candidate from your deck")    

   
        text = input()
        finished = selectOption(text, player, options, level)
    player.hand = []
    player.shield = 0
    if timer==-1:
        battle.makeBattle(player, Enemy(level+1), -1) 
    battle.makeBattle(player, Enemy(level+1), timer+time.time()-startTime)
            

def selectOption(text, player,options, level):
    if text.lower()=="health up":
        print("HP++")
        player.maxHealth+=15
        return True
        
    elif text.lower().find("remove ")!=-1 and len(player.deck)>3:
        text = text.replace("remove ", "")
        success = False
        
        if text.isdecimal() and int(text)<len(player.deck):
            player.removeFromDeck(player.deck[int(text)])
            return True
        
        for card in player.deck:
            if cards.names[card].lower()==text.lower():
                print("removing card")
                player.removeFromDeck(card)
                return True
        if not success:
            print("coundt find a "+text+" card in your deck")
            
    elif text.lower().find("add ")!=-1:
        text = text.replace("add ", "")
        #text = text.replace(" ", "")
        if text=="0" or text=="1" or text=="2":
            player.addToDeck(options[int(text)])
            player.health = player.maxHealth
            return True
        
        for card in options:
             print("checkin card")                  
             if cards.names[card].lower()==text.lower():
                  player.addToDeck(card)
                  player.health = player.maxHealth
                  return True
    return False
         

def createOptions():
    options = []
    for i in range(3):
        done = False
        card = 0
        while not done:
            #the last 2 cards shouldn't show up so that you need to evolve them instead of buying them
            card = random.randrange(0,len(cards.names)-2)
            if options.count(card)==0:
                 done = True
        options.append(card)    
    return options

def printCards(hand):
    #creating the names of the cards
    names = "║"
    for card in hand:
        names+=" "+str(hand.index(card))
        nameSize = len(cards.names[card])+2
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
            line+=" "+effectLine[lineIndex]
            line+=" "*(cardWidth-len(effectLine[lineIndex])-1)+"║"
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
            line+=" "+spellLine[lineIndex]
            line+=" "*(cardWidth-len(spellLine[lineIndex])-1)+"║"
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