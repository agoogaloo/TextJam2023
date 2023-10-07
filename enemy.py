import time


class Enemy:
    def __init__(self, level):
        self.name = "bad guy"
        self.maxHealth = 30+5*level
        self.health = self.maxHealth
        self.damage = 2+level
        self.attackSpeed = 1
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
        