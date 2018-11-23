import random
from functools import reduce
class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

class Game:

    def __init__(self):
        self.cardlist = []          
        self.numberlist = []
    

    @staticmethod
    def game1():
        deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
        random.shuffle(deck)
        card = deck.pop()
        return card
        

    def game2(self):
        self.card = Game.game1()
        self.cardlist.append(self.card)
        
        print("card>>>", self.card)
        print("cardlist>>>", self.cardlist)
    
        self.num = self.card.lstrip(self.card[0])
        print("num>>>", self.num)
        
        if self.num == 'k' or self.num == 'q' or self.num == 'j':
            self.num = 10
        elif self.num == 'a':
            pass
        else:
            self.num = Casting.to_int(self.num)
        
        print("intnum>>>", self.num)
        self.numberlist.append(self.num)
        print("numberlist>>>", self.numberlist)
        
    
    
    def summation(self):
        ret = 0
        a_value = False
        for i in self.numberlist:
            if i == 'a' and a_value == False:
                a_value = input("a를 1로 하겠습니까? -> 1입력 아니면 11로 하겠습니까? -> 11입력")
                if a_value == '11' or a_value == '1':
                    i = int(a_value)
                else:
                    print("다시입력하세요")
                        
            ret += i
        return ret

        self.cardsum = ret
        print("cardsum>>>", self.cardsum)
        return ret


# g = Game()
# g.game2()
# g.game2()
# g.summation()


class Player(Game):
    def play_game(self):
        self.game2()
        self.summation()
        self.game2()
        self.summation()

p = Player()
p.play_game()
        
        
         
# class Dealer(Game):
#     def __init__(self):
#         self.game1()
#         self.cardsummation()
#         while(self.cardsum < 21):
#             self.game1()
#             self.cardsummation()

        
        
#         print(self.cardlist)
#         print("딜러의 카드 총 합>>>",self.cardsum)

# # a.cardlist()
# a = Player()
# b = Dealer() 

# # while(a.cardsum < 21):
    
# #     if a.cardsum == 21:   print("승")

# #     elif a.cardsum > 21:   print("패")

# #     elif a.cardsum < 21:
# #         hitorstand = input("Hit 하고 싶으면 1, Stand 하고 싶으면 2를 입력하세요.")
        
# #         if hitorstand == '1':   
# #             continue

# #         if hitorstand == '2': 
# #             print(a.cardsum)
# #             break



# # while(b.cardsum < 17)

# #     if b.cardsum == 21:   
# #         print(b.cardsum)
# #         break

# #     elif b.cardsum > 21:   
# #         print("player 승")



# print("승패 결과는???????")
# if a.cardsum < b.cardsum :
#     print("승")

# elif a.cardsum == b.cardsum :
#     print("비김")    

# elif a.cardsum > b.cardsum :
#     print("패")  