import random
import cards
class Player:

    def __init__(self, name,deck):
            self.name = name
            self.deck = deck
            self.hand = []
            self.maxHealth = 50
            self.health = self.maxHealth

            self.enemy = None
    def targetEnemy(self, enemy):
         self.enemy = enemy
    def draw(self):   
        
        card = self.deck[random.randrange(0,len(self.deck))]
        self.hand.append(card)
        
    def useCard(self, index):
        cards.functions[self.hand[index]](self)
        self.hand.pop(index)
        self.draw()
        
    def damage(self, dmg):
         self.health-= dmg
         if self.health<=0:
              print("you failed, and the world has been destroyed :(")

    def attack(self, dmg):
        if self.enemy:
            self.enemy.hit(dmg)


    def heal(self, amount):
        print("heal!")
        self.health+=amount
        #capping health to max health
        self.health = min(self.health, self.maxHealth)
 
         
