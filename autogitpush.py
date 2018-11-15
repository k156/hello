import datetime
import os, sys

msg = sys.argv[1]


def autogit():
    os.system("git add --all")
    if msg == False:
        input_msg = input("입력하고 싶은 메세지를 입력하거나 디폴트 메세지로 입력하려면 Enter를 누르세요.")
        if input_msg == False:
            input_msg = (datetime.datetime.now.month, datetime.datetime.now.day)
            os.system("git commit -am '{}-{} 강의'.format(input_msg)")
        else:
            msg_2nd = input_msg
            os.system("git commit -am '{}'.format(msg_2nd)")
    else:
        os.system("git commit -am '{}'.format(sys.argv[1])")
    os.system("git push -u origin master")
