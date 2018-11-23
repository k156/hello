import random
from functools import reduce
import os


class Game:
  
    def __init__(self):

        self.cardlist = []          
        self.numberlist = [] 
        self.cardsum = 0

    
    @staticmethod
    def game1():
        deck = ['♠a','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠j','♠q','♠k',
                '♣a','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣j','♣q','♣k',
                '♥a','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥j','♥q','♥k',
                '◆a','◆2','◆3','◆4','◆5','◆6','◆7','◆8','◆9','◆10','◆j','◆q','◆k']
        random.shuffle(deck)
        card = deck.pop()
        return card
        

    def game2(self):
        self.card = Game.game1()
        self.cardlist.append(self.card)
    
        self.num = self.card.lstrip(self.card[0])
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10

        elif self.num == 'a':
            pass
            
        else:
            self.num = int(self.num)

        self.numberlist.append(self.num)
      

class Player(Game):

    def has_a(self):
        if i == 'a':
            input_a = input ("a의 값 결정 (1 = 1 입력, 11 = 11 입력) >> ")
            if input_a == '1':
                i = 1
            elif input_a == '11':       
                i = 11
        self.cardsum += i


    def __init__(self):
        
        super().__init__()
        self.game2()
        for i in self.numberlist:
            self.has_a()
        
        while( self.cardsum < 21): 
            
            self.game2()

            for x, i in enumerate(self.numberlist):
                
                if len(self.numberlist) >= 2 and x < ( len(self.numberlist) - 1 ): continue 
                self.has_a()


            print("플레이어의 카드>>>", self.cardlist) 
            
            if self.cardsum == 21: 
                os.system('CLS')
                print("플레이어의 카드>>>", self.cardlist) 
                print("플레이어의 카드 총 합>>>", self.cardsum)
                
            elif self.cardsum > 21:
                os.system('CLS')
                print("플레이어의 카드>>>", self.cardlist) 
                print("플레이어의 카드 총 합>>>", self.cardsum) 
                

            elif self.cardsum < 21: 
                hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.") 


                if hitorstand == '1': 
                    continue 


                elif hitorstand == '2':  
                    os.system('CLS')
                    print("플레이어의 카드>>>", self.cardlist) 
                    print("플레이어의 카드 총 합>>>", self.cardsum) 
                    break 
     
         
class Dealer(Game):
    def __init__(self):
        
        super().__init__()
        self.game2()
        for i in self.numberlist:
            if i == 'a':
                if (21 - self.cardsum) < 10:
                    i = 11
                else : 
                    i = 1
            self.cardsum += i
        

        while( self.cardsum < 17 ):
            
            self.game2()
            
            for x, i in enumerate(self.numberlist):
                
                if len(self.cardlist) > 2 and x < ( len(self.cardlist) - 1 ): continue 
                
                if i == 'a':
                    if (21 - self.cardsum) < 10:
                        i = 11
                    else : 
                        i = 1
            
            self.cardsum += i
        
        print("\n")
        print("딜러의 카드리스트>>>",self.cardlist)
        print("딜러의 카드 총 합>>>",self.cardsum)


#============= MAIN =================


def over_21(a,b):
    if a < 21 and b < 21:
        if a > b : print("승") 
        elif a == b : print("비김")
        elif a < b : print("패")
    
    elif a < 21 and b > 21:  print("승")       
    elif a > 21 : print("패")
    elif a == 21 : print("승")
    elif a != 21 and b == 21: print("패")   


while(True):
    
    start_game = input("게임을 시작하려면 엔터를 누르세요")
    os.system('CLS')

    if start_game == '':
        
        a = Player()
        b = Dealer() 

        print("\n승패 결과는???????") 
        over_21(a.cardsum, b.cardsum)
        
    else : break    
    

         

#============= FLOW =================