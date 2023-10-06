import cards

cardWidth = 25

def makeBattle(player):
    finished = False
    #draw 3 random starting cards
    for i in range(3):
        player.draw()

    while not finished:
        printBattle(player.hand, player)
        text = input()
        doActions(text, player)
        if text == "done!":
            finished = True

def printBattle(hand, player):
  
        #border = " "+"-"*((cardWidth+1)*len(hand)-1)+" "
        border = " "+(("-"*cardWidth)+" ")*len(hand)
        splitBorder = "|"+(("-"*cardWidth)+"|")*len(hand)
        incantationHeader = "|"+((" "*6)+"-INCANTATION-"+" "*6+"|")*len(hand)
        status = "  -STATUS-   HP: "+str(player.health)+"/"+str(player.maxHealth)

        #creating the names of the cards
        names = "|"
        for card in hand:
            nameSize = len(cards.names[card])
            spaceUsed =int((cardWidth-nameSize)/2)
            names+=" "*(spaceUsed)
            names+=cards.names[card]
            spaceUsed+=nameSize
            names+=" "*(cardWidth-spaceUsed)
            names+="|" 

        #creating effects row
    
        effects = []
        effectLines = []
        for effect in cards.effects:
             effectLines.append(effect.split("\n"))
        finishedText = False
        lineIndex = 0
        while not finishedText:
            line = "|"
            finishedText= True
            for card in hand:
                effectLine = effectLines[card]
                if lineIndex>=len(effectLine):
                    line+=" "*cardWidth+"|"
                    continue
                line+=effectLine[lineIndex]
                line+=" "*(cardWidth-len(effectLine[lineIndex]))+"|"
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
            line = "|"
            finishedText= True
            for card in hand:
                spellLine = spellLines[card]
                if lineIndex>=len(spellLine):
                    line+=" "*cardWidth+"|"
                    continue
                line+=spellLine[lineIndex]
                line+=" "*(cardWidth-len(spellLine[lineIndex]))+"|"
                finishedText = False
            if not finishedText:
                spells.append(line)
            lineIndex+=1
            
        #adding all the lines into one array (creating the actual menu)
        lines = [status,border,names,splitBorder]
        for line in effects:
             lines.append(line)
        lines.append(splitBorder)
        lines.append(incantationHeader)
        lines.append(splitBorder)
        for line in spells:
             lines.append(line)
        lines.append(border)
        print("\n")
        for line in lines:
            print(line)

def doActions(text, player):
    hand = player.hand
    for i in range(len(hand)-1,-1,-1):
        print(i)
        if text == cards.spells[hand[i]].replace("\n"," "):
            player.useCard(i)
        else :
            print(text +"is different than \n"+cards.spells[hand[i]].replace("\n"," "))
        
