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
            cards.setWorldName(name)
    def targetEnemy(self, enemy):
         self.enemy = enemy
    def draw(self, startHand = False): 
        megumin = True    
        #making it so you cant draw megumin in the starting hand because thats too strong     
        while megumin:
            megumin = False
            if len(self.cardsToDraw)==0:
                self.cardsToDraw = self.deck.copy()
                print("reshuffling")
            index = random.randrange(0,len(self.cardsToDraw))
            card = self.cardsToDraw[index]
            if startHand and cards.names[card]=="Crimson Demon":
                print("not letting you start with that one"+str(card)+str(self.cardsToDraw))
                self.cardsToDraw.pop(index)
                #Summon before me the root of thy power hidden within the lands of the kingdom of demise! EEEXPLOSION!!!
                megumin = True
            
        self.hand.append(card)
        self.cardsToDraw.pop(index)
        print("Deck:" +str(self.deck)+" undrawn cards:"+str(self.cardsToDraw))
       
       
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
        
        oneShot = function(self)
        self.hand.pop(index)
        return oneShot
    
        
    def damage(self, dmg):
        print("dealing "+str(dmg)+" damage to "+str(self.shield)+" shield")
        self.shield-=dmg

        if self.shield<0:
            self.health+= self.shield
            self.shield = 0

        if self.health<=0:
            print("you failed, and the world has been destroyed :(")
    def stun(self, time):
        self.enemy.overTime-=time

    def attack(self, dmg):
        print("attacking with "+str(dmg))
        if self.enemy:
            self.enemy.hit(dmg)

    def addShield(self, amount):
         self.shield+=amount

    def heal(self, amount):
        print("heal!")
        self.health+=amount
        #capping health to max health
        self.health = min(self.health, self.maxHealth)
 
         
