import struct


labelFile = open("./data/" + name + "-labels-idx1-ubyte", "rb")
imageFile = open("./data/" + name + "-images-idx3-ubyte", "rb")



magicNo, labelCnt = struct.unpack(">II", labelFile.read(8)) # I 는 unsigned int, 4byte. I가 두개니까 read(8). 첫번째 4byte는 magicNo, 두번재는 lableCnt에 담음. 이 정보는 자료 제공자가 명시해뒀음.
magicNo, imageCnt = struct.unpack(">II", imageFile.read(8))
rows, cols = struct.unpack(">II", imageFile.read(8))
pixels = rows * cols            # 28 X 28

for i in range(labelCnt):
    alabel = struct.unpack("B", labelFile.read(1))[0] #앞에 두 개를 unpack했고 그 다음부터는 레이블.
    imgdata = list(map(lambda b: str(b), imageFile.read(pixels))) # map은 어레이의 인자를 하나씩 b에 줘서 str으로 만들어준 후 리스트에 append됨.

    csvFile.write(str(label) + ",")
	csvFile.write(",".join(imgdata) + "\r\n")

# for j, x in enumerate(imgdata):
#     if j % 28 == 0:
#         print("\n")
#     print('{:4s}'.format(str(x)), end='') #데이터확인


