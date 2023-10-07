import random
import cards
class Player:

    def __init__(self, name,deck):
            self.name = name
            self.deck = deck
            self.cardsToDraw = deck.copy()
            self.hand = []
            self.maxHealth = 50
            self.health = self.maxHealth

            self.enemy = None
    def targetEnemy(self, enemy):
         self.enemy = enemy
    def draw(self): 
        if len(self.cardsToDraw)==0:
            self.cardsToDraw = self.deck.copy()
            print("reshuffling")
        print(self.cardsToDraw) 
        print("deck:"+str(self.deck))
        index = random.randrange(0,len(self.cardsToDraw))
        card = self.cardsToDraw[index]
        self.hand.append(card)
        self.cardsToDraw.pop(index)
        print(self.cardsToDraw)
       
       
    def addToDeck(self, card):
        self.deck.append(card)
        self.cardsToDraw.append(card)

    def removeFromDeck(self, card):
        self.deck.remove(card)
        if self.cardsToDraw.count(card)>0:
            self.cardsToDraw.remove(card)

    def useCard(self, index):
        cards.functions[self.hand[index]](self)
        self.hand.pop(index)
    
        
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
 
         
