cmd = input ("이름,나이,성별")
if cmd == "":
    print("정확히 입력해주세요.")
    exit()
cmds = [cmd.split(',')]
if len(cmds) != 3:
    print ("세 항목 다 입력해주세요.")
    exit()
outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다."

print(outmsg.format(cmds[0], cmds[1], cmds[2]))