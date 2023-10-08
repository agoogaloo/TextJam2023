
import random

easyNames = ["slime", "goblin", "anomura"]
hardNames = ["Brachyura", "dragon", "demon"]

class Enemy:
    def __init__(self, level):
        if level==9:
            self.name = "Demon King"
        elif level<=4:
            self.name = easyNames[random.randrange(0,len(easyNames))]
        else:
            self.name = hardNames[random.randrange(0,len(hardNames))]
        
        self.maxHealth = 30+5*level
        self.health = self.maxHealth
        self.damage = 2+int(level/2)
        self.attackSpeed = 2-level/10
        self.overTime = -self.attackSpeed
        self.level = level


    def hit(self, dmg):
        self.health-=dmg

    def doActions(self, time, player):
        time+=self.overTime
        while time>self.attackSpeed:
            self.attack(player)
            time-=self.attackSpeed
           
        self.overTime = time
       
    def attack(self, player):
        if self.health<=0:
            return
        player.damage(self.damage)
        print(self.name+" hit for "+str(self.damage)+" and killed all the heros")
        print("the world has "+str(player.health)+"/"+str(player.maxHealth)+" hp left")
        