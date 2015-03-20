import user
import engine
class Code(object):
    def start(self):

        self.intro()
        self.y = user.User()
        self.insert()

    def intro(self):
        print "Welcome! said a voice from the end of the dark room."
        print "You have to bee the first person I've met in years"
        print " who dare to scape."
        print "If you want to get through the exit, you will need to type the code."
        print "I may advice you to seach for it before trying out."


    def insert(self):
        self.code = int(self.y.inputs())
        self.compare(self.code)

    def compare(self, code):
        elemetns = self.y.getElement()
        
        try:
            index = elemetns.index("code")
        
            if code == int(elemetns[index + 1]):
                print "You have done the imposible and sabe yourself from the dark room."
                

            else:
                print " The door doesn't even move a feet."
                self.en = engine.Engine().game()
        except Exception, e:
            print "you do need to search for the code, as it will be imposible to open the door if not."
            self.en = engine.Engine().game()

if __name__ == '__main__':  
    x = Code()
