import cards
import gameOver
import shop
import win
import enemy as Enemy

import time

cardWidth = 25

def makeBattle(player, enemy, timer):
    finished = False
    starting = True
    
    player.targetEnemy(enemy)
    #draw 3 random starting cards
    for i in range(player.handSize):
        player.draw(True)

    exitFunc = None
    enemyAttack = enemy.getWaitingQuote()
    while not finished:
        printBattle(player.hand, player, enemy, timer)
        print(enemyAttack)
        startTime = time.time()
        text = input()
        timeTaken = time.time()-startTime
        if timer!=-1:
            timer+=timeTaken
        #not letting the enemy attack until you have done something
        if starting:
            timeTaken = 0
            starting = False
        #enemy attack
        enemyAttack = enemy.doActions(timeTaken, player)
        #player attacks
        doActions(text, player)

        if player.health<=0:
            finished = True
            exitFunc = gameOver.finishGame
        elif enemy.health<=0:
            finished = True
            if enemy.level==Enemy.bossLevel:
                exitFunc = win.winGame
            else:
                exitFunc = shop.openShop
        

    enemy.health=0
    exitFunc(player, enemy.level, timer)
    

        

def printBattle(hand, player, enemy, time):
  
        #border = " "+"-"*((cardWidth+1)*len(hand)-1)+" "
        border = " "+(("═"*cardWidth)+" ")*len(hand)
        incantationHeader = "║"+((" "*6)+"-INCANTATION-"+" "*6+"║")*len(hand)
        status = "  |  -"+player.name.upper()+"-  HP: "+str(player.health)+"/"+str(player.maxHealth)+"   SHIELD: "+str(player.shield)
        splitBorder = "║"+(("-"*cardWidth)+"║")*len(hand)
        enemyStats = "  |  -"+enemy.name.upper()+"-  HP: "+str(enemy.health)+"/"+str(
            enemy.maxHealth)+"  ATK: "+str(enemy.damage)+" DMG/{:.1f} SEC".format(enemy.attackSpeed)
        if enemy.overTime<0:
            enemyStats+="  STN: {:.1f}".format(-enemy.overTime)
        enemyStats+=" "*(63-len(enemyStats))+"|"
        status+=" "*(63-len(status))+"|"
        statusBorder = "   "+"─"*60

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
        lines.append(status)
        lines.append(enemyStats)
        lines.append(statusBorder)
        print("\n\n\n")
        if time!=-1:
            print("TIME: {:.3f} sec.".format(time))
        print("  -- LEVEL "+str(enemy.level)+" --")
        for line in lines:
            print(line)

def doActions(text, player):
    hand = player.hand
    for i in range(len(hand)-1,-1,-1):
        if text == cards.spells[hand[i]].replace("\n"," "):
            card = player.hand[i]
            x = player.useCard(i)
            print(x)
            if x:
                while player.hand.count(card)>0:
                    player.hand.remove(card)
                    player.draw()
                return
            
        
