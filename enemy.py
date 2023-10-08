
import random

easyNames = ["Slime", "Spider", "Anomura"]
easyAttacks = [["bounced around","squished menacingly"],["scuttled around","jumped way higher than it should be able to"],
               ["wished to was a crab", "clacked weakly", "probably isnt turing complete"]]
easyDeaths = ["the heros felt sorry and left","the heros were scared away","the heros somehow got lost",
              "the heroes found a sidequest to do instead","the heroes go on a beach episode"]
hardNames = ["Brachyura", "Dragon", "Demon"]
hardAttacks = [["clicked and clacked", "used its crab powers"],["started a bunch of fires", "flies around"],["is being a bad guy"]]
hardDeaths = ["the heros were burned to a crisp","the heroes got crushed","the heroes forgot the power of friendship",
              "the heroes wished they would stop getting reincarnated","the heroes didn't get back up"]
bossAttacks = ["sends his regards", "went all out just this once", "is destroying everything"]

waitingLines = ["is waiting for something to happen", "is standing there peacefully", "looks lost in thought", 
                "doesnt notice you","is standing there menacingly"]

kingLevel = 3
easyLimit = 1

class Enemy:
    def __init__(self, level):
        if level==kingLevel:
            self.name = "The Demon King"
        elif level<=easyLimit:
            self.name = easyNames[random.randrange(0,len(easyNames))]
        else:
            self.name = hardNames[random.randrange(0,len(hardNames))]
        
        self.maxHealth = 30+5*level
        self.health = self.maxHealth
        self.damage = 2+int(level/2)
        self.attackSpeed = 2-level/10
        self.overTime = -self.attackSpeed
        self.level = level

    def getWaitingQuote(self):
        return self.name+" "+waitingLines[random.randrange(0,len(waitingLines))]

    def hit(self, dmg):
        self.health-=dmg

    def doActions(self, time, player):
        time+=self.overTime
        damage = 0
        while time>self.attackSpeed:
            damage+=self.attack(player)
            time-=self.attackSpeed
           
        self.overTime = time

        description = "   - "+self.name+" "
        if self.level==kingLevel:
            description+=bossAttacks[random.randrange(0,len(bossAttacks))]
            description+="\n     -dealt "+str(damage)+" damage and "
            description+=hardDeaths[random.randrange(0,len(hardDeaths))]+"."
        elif self.level<=easyLimit:
            index = easyNames.index(self.name)
            description+= easyAttacks[index][random.randrange(0,len(easyAttacks[index]))]
            description+="\n     -dealt "+str(damage)+" damage and "
            description+=easyDeaths[random.randrange(0,len(easyDeaths))]+"."
        else:
            index = hardNames.index(self.name)
            description+= hardAttacks[index][random.randrange(0,len(hardAttacks[index]))]
            description+="\n     -dealt "+str(damage)+" damage and "
            description+=hardDeaths[random.randrange(0,len(hardDeaths))]+"."

        return description
       
    def attack(self, player):
        if self.health<=0:
            return 0 
        player.damage(self.damage)
        return self.damage