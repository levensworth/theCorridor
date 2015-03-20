import user
import engine
class Beer(object):
    def start(self):
        self.intro()
        self.y = user.User()
        self.buy()


    def intro(self):
        print """
            Hey, you! HI!
            My name is mordo, I'm the bar tender here, many people came just to buy a beer from
            ver far lands. That's cause my beer is the BEST!.
            jajaja d'you want one?


        """

    def buy(self):
        want = self.y.inputs()

        if "yes" in want:
            self.money = self.y.getElement()
            
            if "money" in self.money:
                index = self.money.index("money")
                self.beer(index)
            else:
                print "Men, you need money to buy one!"
                self.en = engine.Engine().game()
        else:
            print "Well I suppose you don't have enough money!"
            self.en = engine.Engine().game()

    def beer(self, index):
        self.actualMoney = self.y.getElement()
        self.amount = self.actualMoney[index + 1]
        if float(self.amount) > 10 :
            self.y.setElement(("beer"))
            print "Here you have, you know?.....erlier this morning a wizard came for one."
            print "But he couldn't afford it, I think he might like one."
            self.en = engine.Engine().game()
        else:
            print "sorry man but you need at least 10 gold coins."
            self.en = engine.Engine().game()



if __name__ == "__main__":
    x = Beer()
