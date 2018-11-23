

    
    def has_jqk(self):
        self.numberlist = [] 
        if self.num != 'j' and self.num != 'q' and self.num != 'k' and self.num != 'a':
            self.num = Casting.to_int(self.num)
            self.numberlist.append(self.num)
    
        else:
            self.cardlist.append(10)

        print(self.numberlist) 

    def summation(self):
        self.cardsum = reduce(lambda x, y: x + y, self.numberlist)             
        print(self.cardsum)


a = Card()


class Player(Card):
    def __init__(self):
        super().__init__()
        super().has_jqk()
        if self.num == 'a':
            while (a_value == False):
                a_value = input("A값을 1과 11중에 선택하세요.")
                if a_value == 1:
                    self.num = 1
                elif a_value == 11:
                    self.num = 11
                else:
                    continue
        super().summation()
       



a = Card()
p = Player()