import user
import random
class Room(object):
    def code(self):
        self.code = random.random()
        val = self.truncate(self.code, 7)
        return str(val)

    def truncate(self,f, n):
        number = f
        decimal = str(number)[:n]
        decimal = decimal[2:]
        return decimal

    

if __name__ == '__main__':
    x = Room()
    x.code()
