import duelling
import gold
import beer
import code
import user
import corridor
class Engine( object):

    def __init__ (self):
        passage = corridor.Corridor()
        gold_room = gold.Gold()
        duelling_room = duelling.Duel()
        beer_room = beer.Beer()
        player = user.User()
        code_room = code.Code()
        self.rooms = {'passage' :passage,'gold_room':gold_room, 'duelling_room' :duelling_room, 'beer_room' :beer_room, "code_room": code_room}
        self.intro()
        self.game()
    
    def next_room(self,room):
       
        self.rooms[room].start()
        

    def getIndex(self,room):
        return self.rooms.index(room)


    def game(self):
        room = self.rooms["passage"].start()
        self.next_room(room)

    def intro(self):
        print "-------------------------------------------------"

# put a return to this class in each module

if __name__ == '__main__':
    x = Engine()
