import time


class Enemy:
    def __init__(self):
        self.name = "bad guy"
        self.maxHealth = 30
        self.health = self.maxHealth
        self.damage = 2
        self.attackSpeed = 1
        self.overTime = -self.attackSpeed


    def hit(self, dmg):
        self.health-=dmg

    def doActions(self, time, player):
        print("doing "+str(time)+" attacks + "+str(self.overTime)+" from last turn")
        time+=self.overTime
        while time>self.attackSpeed:
            self.attack(player)
            time-=self.attackSpeed
            print(str(time)+"time left to simulate")
        self.overTime = time
        print(str(self.overTime)+" time left over")
       
    def attack(self, player):
        if self.health<=0:
            return
        player.damage(self.damage)
        print(self.name+" hit for "+str(self.damage)+" and killed all the heros")
        print("the world has "+str(player.health)+"/"+str(player.maxHealth)+" hp left")
        