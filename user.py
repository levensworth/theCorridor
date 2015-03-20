import csv
class User(object):
    
    
   
    
    def inputs (self):
        userData = raw_input("> ")
        return userData

    
       
    def setElement (self, element):    
        player_writer = open('player.csv','a')
        
        
        player_writer.write(element)
        
        player_writer.write('\n')
        player_writer.close()

    def getElement (self):
        player = open('player.csv','a+')
        current_player = []
        for lines in player:
            data = lines.split()
            current_player.append(data[0])
        player.close()
        return current_player
    
    def removeElement(self, element):
        
        game_user = self.getElement()
        player = open('player.csv','w')
        game_user.remove(element)
        for x in game_user:

            player.write(x+' ')
        player.close()


if __name__ == '__main__':
    x = User()
    x.setElement('test')
    x.setElement('money')
    
    print x.getElement()
    x.removeElement('test')
