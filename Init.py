class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age



    def walk(self):
        print(self.name,'can walk')
        print(self.name,'is',self.age,'\n')

s1=Students('jesse','18')
s1.walk()

s2=Students('james','15')
s2.walk()