exo = ["김준면", "오세훈", "김민석", "김종인", "김종대", "변백현", "박찬열", "도경수")
kims = filter(lambda x: x == exo.find("김"), exo)
print(list(kims))
