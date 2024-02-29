from math import sqrt

def somme(x,y):
    return x+y

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def afficher(self):
        print("Point:",self.x,",",self.y)
    def __str__(self):
        return "Point:"+str(self.x)+","+str(self.y)
    def decaler(self, dx, dy):
        self.x+=dx
        self.y+=dy
    def distance(self,p):
        dx=(self.x-p.x)
        dy=(self.y-p.y)
        d2=sqrt(dx**2+dy**2)
        return d2        