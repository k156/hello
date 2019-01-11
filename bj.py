import reduce

class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s.strip())
        else:
            return s

    def __str__(s):
        return s

class Deck:
    def randomcard ():
        import random
        deck = ['sa','s2','s3','s4','s5','s6','s7','s8','s9','s10','sj','sq','sk','ca','c2','c3','c4','c5','c6','c7','c8','c9','c10','cj','cq','ck','ha','h2','h3','h4','h5','h6','h7','h8','h9','h10','hj','hq','hk','da','d2','d3','d4','d5','d6','d7','d8','d9','d10','dj','dq','dk']
        random.choice(deck)

class Game:
    while (cardsum <21):
        def game1(self):
            card = Deck.randomcard(deck)
            cardlist = list.append(card)
            numberlist = []
            
            print(cardlist)
            
            for i in range(4):
            card.lstrip('{}'.format(shape))
            shape = ['s','c','h','d']        
            
            has_jqk = filter(lambda x: type(x[1]) = str, cardlist)
            if has_jqk == True:
                numberlist.append(10)

            has_a = filter(lambda x: x[1] == "a", cardlist)
            if has_a == True:
                while (a_value != 1 and a_value != 11):
                    a_value = input("A값을 1과 11중에 선택하세요.")
                    if a_value == 1:
                        numberlist.append(1)
                    elif a_value == 11:
                        numberlist.append(11)
                
        def game2(self):
            self.game1()
            numberlist = []
            numberlist.append(Casting.to_int(card))
            cardsum = reduce(lambda x, y: x + y, numberlist)


class Player(Game):

        super().game2()
        if cardsum == 21:
            print("승")
        if cardsum > 21:
            print("패")
        if cardsum < 21:
            super().game1()
            hit = input("카드를 더 받으려면 'hit', 그만 받으려면 'stand'를 입력하세요.")
            if hitorstand == 2:
                break
                if Dealer.cardsum < Player.cardsum:
                    print("승")
                if Dealer.cardsum > Player.cardsum:
                    print("패")


    

    game()
    if cardsum == 21:
        print("승")
    elif cardsum > 21:
        print("패")
    else:
        while (cardsum <21):
            hitorstand = input("카드를 더 받으려면 'hit', 그만 받으려면 'stand'를 입력하세요.")
            if hitorstand == 'stand':
                break
                if Dealer.cardsum == Player.cardsum:
                    print("비겼습니다.")
                elif Dealer.cardsum > Player.cardsum:
                    print("패")
                else:
                    continue
                
                                        


class Dealer(Game):
super().game2()
def reveal(self):
    print(card1)
        
if cardsum > 17:
    break
