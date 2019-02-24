

class Father:
    name='jesse'
    def eat(self):
        print("I can eat")
class Mother:
    def walk(self):
        print('walk like mother')

class Son(Father,Mother):
    def eat(self):
        print('eat like son')
    def walk(self):
        print('walk like 11')

littleJesse=Son()
littleJesse.walk()