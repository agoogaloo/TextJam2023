import random
import cards
class Player:

    def __init__(self, deck):
            self.deck = deck
            self.hand = []

            self.maxHealth = 15
            self.health = self.maxHealth
    def draw(self):   
        
        card = self.deck[random.randrange(0,len(self.deck))]
        print("drawing card "+str(card))
        self.hand.append(card)
        
    def useCard(self, index):
        print("using card number "+str(index))
        cards.functions[self.hand[index]](self)
        self.hand.pop(index)
        self.draw()
        

    def attack(self, dmg):
        print("attack!")


    def heal(self, amount):
        print("heal!")
        self.health+=amount
        #capping health to max health
        self.health = min(self.health, self.maxHealth)
 
         
