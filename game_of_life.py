#import pygame
import time
import random
class World():
    def __init__(self, n=30, m=30):
        self.width=n
        self.height=m
        self.map=[]
    def map_gen(self, m=None):
        if(not m):
            m=[]
            for i in range(self.width * self.height // 10):
                x=random.randint(0, self.width)
                y=random.randint(0, self.height)
                while [x, y] in m:
                    x=random.randint(0, self.width)
                    y=random.randint(0, self.height)
                m.append([x, y])
        self.map=m.copy()
        return 0
    def live_neighbour(self, x, y):
        l=0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if([i, j] in self.map):
                    l+=1
        if ([x, y] in self.map):
            l-=1
        return l
    def evalute(self):
        p=[]
        for i in range(self.height):
            for j in range(self.width):
                l=self.live_neighbour(i, j)
                if (([i, j] in self.map) and (l==2 or l==3)):
                    p.append([i, j])
                if (not [i, j] in self.map and l==3):
                    p.append([i, j])
        self.map=p.copy()
    def draw(self):
        print("\033[H")
        for i in range(self.height):
            for j in range(self.width):
                if ([i, j] in self.map):
                    print("@", end='')
                else:
                    print(" ", end='')
            print("")
    def run(self):
        while True:
            self.draw()
            self.evalute()
            #time.sleep(0.2)
            c=input()
a=World()
a.map_gen()
a.run()
