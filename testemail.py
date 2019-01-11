a= "보낼 메시지"

import smtplib
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP('smtp-mail.outlook.com', 587) #gmail은 (smtp.gmail.com,587)
smtp.ehlo()      # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('자기 아이디 입력', '자기 비번 입력')
 
msg = MIMEText(a)
msg['Subject'] = '제목'
msg['To'] = '보낼 메일주소'
smtp.sendmail('보낼 메일주소', '받는 메일주소', msg.as_string())
 
smtp.quit()