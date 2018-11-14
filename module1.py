import datetime
import os
import sys

msg = sys.argv([1])


def add_commit_push():
    cd c:\workspace\hello
    os.system("git add --all")
    if msg == false:
        input_msg = input("입력하고 싶은 메세지를 입력하거나 디폴트 메세지로 입력하려면 Enter를 누르세요.")
        else:
            os.system("git commit -am '{}-{} 강의'.format(msg)")
            if input_msg == false:
                input_msg = (datetime.datetime.now.month, datetime.datetime.now.day)
                os.system("git push -u origin master")