
import random

easyNames = ["Anomura","Slime", "Spider"]
easyAttacks = [["wished to was a crab", "clacked weakly", "probably isnt turing complete"],
               ["bounced around","befriends a dragon","squished menacingly"],
               ["scuttled around","has gross hairs","jumped way higher than it should be able to"],
]
easyDeaths = ["felt sorry and left","were scared away","somehow got lost",
              "found a sidequest to do instead","left to go on a beach episode"]
hardNames = ["Brachyura", "Dragon", "Demon"]
hardAttacks = [["clicked and clacked", "used its crab powers"],["started a bunch of fires", "flies around"],["is being a bad guy"]]
hardDeaths = ["were burned to a crisp","got crushed","forgot the power of friendship",
              "wished they would stop getting reincarnated","didn't get back up"]
bossAttacks = ["sends his regards", "went all out just this once", "is destroying everything"]

waitingLines = ["is waiting for something to happen", "is standing there peacefully", "looks lost in thought", 
                "doesnt notice you","is standing there menacingly"]
stunLines = ["forgets who they are", "is stunned", "stands still so you don't see them"]

bossLevel = 7
easyLimit = 3

class Enemy:
    def __init__(self, level):
        self.overTime = 0
        self.level = level

        #default stats
        self.maxHealth = 30+5*level
        
        self.damage = 2+int(level/2)
        self.attackSpeed = 2-level/10
        
        nameindex = -1
        if level%bossLevel==0:
            self.name = "The Demon King"
            self.maxHealth = 15*level-5
            self.damage = int(1.5*level)
            self.attackSpeed = 2

        elif level<=easyLimit:
            nameindex = random.randrange(0,len(easyNames))
            self.name = easyNames[nameindex]

            self.maxHealth = 30+5*level
            self.damage = 2+int(level/2)
            self.attackSpeed = 2.4-level/5
        else:
            nameindex = random.randrange(0,len(easyNames))
            self.name = hardNames[nameindex]

            self.maxHealth = 10+10*level
            self.damage = level
            self.attackSpeed = 0.25+6/level
        #class stat boosts
        if nameindex==0:
            self.maxHealth+=level+random.randrange(0,level+1)
        if nameindex==1:
            self.damage+= int((level+random.randrange(0,level+1))/10.0)
        if nameindex==2:
            self.attackSpeed/=1+((level+random.randrange(0,level+1))/30.0)

        self.health = self.maxHealth
        
       

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

        #creating a random action based on the monster type
        attack = ""
        deaths = ""
        if self.level%bossLevel==0:
            attack = bossAttacks[random.randrange(0,len(bossAttacks))]
            deaths = hardDeaths[random.randrange(0,len(hardDeaths))]+"."
        elif self.level<=easyLimit:
            index = easyNames.index(self.name)
            attack = easyAttacks[index][random.randrange(0,len(easyAttacks[index]))]
            deaths = easyDeaths[random.randrange(0,len(easyDeaths))]+"."
        else:
            index = hardNames.index(self.name)
            attack = hardAttacks[index][random.randrange(0,len(hardAttacks[index]))]
            deaths = hardDeaths[random.randrange(0,len(hardDeaths))]+"."

        description = "   - "+self.name+" "
        if self.overTime<0 and damage==0:
            description+=stunLines[random.randrange(0,len(stunLines))]
            description+="\n     -the heroes still "+deaths
        else:
            description+=attack
            description+="\n     -dealt "+str(damage)+" damage and the heroes "+deaths
        return description
       
    def attack(self, player):
        if self.health<=0:
            return 0 
        player.damage(self.damage)
        return self.damage