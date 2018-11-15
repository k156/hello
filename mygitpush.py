import datetime
import os, sys


msg = ""
if len(sys.argv) > 1:
    msg = sys.argv[1]

def autogit():
    os.system("git add --all")
    if msg == '':
        input_msg = input("입력하고 싶은 메세지를 입력하거나 디폴트 메세지로 입력하려면 Enter를 누르세요.")
        if input_msg == False:
            auto_msg = (datetime.datetime.now.month, datetime.datetime.now.day)
            os.system("git commit -am '{}-{} 강의'.format(auto_msg)")
        else:
            msg_2 = input_msg
            os.system("git commit -am '{}'.format(msg_2)")
    else:
        os.system("git commit -am '{}'.format(msg)")
    os.system("git push -u origin master")
    exit()


autogit()