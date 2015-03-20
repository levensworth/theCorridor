import random
import os
import user
import room
import engine

class Duel (object):
    # When using __init__() the momet you create the object by instacing it you are also calling the function().
    def start(self):
        self.y = user.User()
        self.enemy = Wizzard()
        self.elements  = self.y.getElement()
        if "beer" in self.elements :
            self.enemy.drink()
        else:
            self.rules()
            raw_input("press ENTER to start > ")
            self.battle()

    def rules (self):
        print """
            There is a wizzard in the corner of the room. He is pointing at you as you make your way into the room.
            "You must defeat me in battle before you leave this place." he shouts.
            ------------------------------------------------------------------------------------------------
            You must type the correct spell to conteracttack his.
            they are:
                    - riptumsempra (for the selthin spell).
                    - retrivio ( for the polymorf spell).
                    - expellia ( for the rootellia spell).
        """
        print ' Good luck.'


    def battle(self):
        wins = 0
         # clear the window so that the user can't cheat.
        os.system('cls' if os.name == 'nt' else 'clear')
        while wins < 3:
            
            self.attack = self.enemy.attack()
            self.react = self.enemy.cast(self.attack)
            print self.attack
            self.user_attack = self.y.inputs()
            if self.react in self.user_attack:
                print 'Well done!'
                wins += 1
            else:
                print 'Wrong spell'
        print "You have defeat me .....in retrieve I gave you the key to access the gold room"
        self.key()
        self.en = engine.Engine().game()


    def key (self):
        print 'take key'   
        self.y.setElement("key")



class Wizzard (object):
    def attack(self):
        self.spell = ["selthin", "polymorf","rootellia"]
        self.selected =self.spell[random.randint(0,len(self.spell)-1)]
        return self.selected

    def cast (self,spell_made):
        self.book = {"selthin":"riptumsempra", "polymorf":"retrivio", "rootellia":"expellia"}
        return self.book[spell_made]


    def drink(self):
        print "hey, you have a beer?"
        print "can I have a drink?"
        if "yes" in raw_input("> "):
            print "Thanks men! I needed"
            print "take, in return I'll tell you the secret code to exit."
            self.r = room.Room()
            self.code = self.r.code()
            print self.code
            y = user.User()
            y.setElement("code")
            y.setElement(self.code)
            print y.getElement()
            
            self.en = engine.Engine().game()

if __name__ == "__main__":
    x = Duel().start()
