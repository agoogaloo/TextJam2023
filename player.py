import random
import cards
class Player:

    def __init__(self, name,deck, maxHealth):
            self.name = name
            self.deck = deck
            self.cardsToDraw = deck.copy()
            self.hand = []
            self.maxHealth = maxHealth
            self.health = self.maxHealth
            self.shield = 0
            self.handSize = 3

            self.enemy = None
    def targetEnemy(self, enemy):
         self.enemy = enemy
    def draw(self): 
        if len(self.cardsToDraw)==0:
            self.cardsToDraw = self.deck.copy()
            print("reshuffling")
        index = random.randrange(0,len(self.cardsToDraw))
        card = self.cardsToDraw[index]
        self.hand.append(card)
        self.cardsToDraw.pop(index)
       
       
       
    def addToDeck(self, card):
        self.deck.append(card)
        self.cardsToDraw.append(card)

    def removeFromDeck(self, card):
        if self.deck.count(card)>0:
            self.deck.remove(card)
        if self.cardsToDraw.count(card)>0:
            self.cardsToDraw.remove(card)

    def useCard(self, index):
        function = cards.functions[self.hand[index]]
        self.hand.pop(index)
        oneShot = function(self)
        return oneShot
    
        
    def damage(self, dmg):
        print("dealaing "+str(dmg)+" to "+str(self.shield)+" shield")
        self.shield-=dmg

        if self.shield<0:
            self.health+= self.shield
            self.shield = 0

        if self.health<=0:
            print("you failed, and the world has been destroyed :(")

    def attack(self, dmg):
        if self.enemy:
            self.enemy.hit(dmg)

    def addShield(self, amount):
         self.shield+=amount

    def heal(self, amount):
        print("heal!")
        self.health+=amount
        #capping health to max health
        self.health = min(self.health, self.maxHealth)
 
         
