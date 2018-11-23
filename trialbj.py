class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

    def __str__(s):
        return s
        
        
import random
from functools import reduce


deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']


class Card:
  
    def __init__(self):
        
        global deck
        random.shuffle(deck)
        self.cardlist = []
        self.cardlist.append(deck.pop())

        
        print(self.cardlist)
        

a = Card()
a = Card()


