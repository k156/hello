with open("ppl.csv", "w", encoding ='utf8') as file:
    file.write("김정민,여,28,90\n")
    file.write("김준면,남,28,92\n")
    file.write("김민석,남,29,89\n")
    file.write("김종대,남,27,79\n")
    file.write("변백현,남,27,82\n")
    file.write("김종인,남,25,87\n")
    file.write("오세훈,남,25,90\n")
    file.write("도경수,남,26,84\n")
    file.write("박찬열,남,27,85\n")
    file.write("장이씽,남,28,81")

with open("ppl.csv", "r", encoding='utf8') as file:
    for line in file:
        print(line)


  def __str__(self):
        return "{}:{}".format(self.name, self.score)


