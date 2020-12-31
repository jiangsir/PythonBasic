import os
import sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


COMMASPACE = ', '
subject = '高師大附中 109學年度國際運算思維挑戰賽 挑戰證明'
from_addr = "mailer@zerojudge.tw"
app_passwd = "zridfkvaolgtoekp"
to_addr = [""]
to_domain = 'stu.nknush.kh.edu.tw'

# attachePath = 'C:\\Users\\user\\Downloads\\109Bebras成績證明\\'
attachePath = '/mnt/c/Users/user/Downloads/109Bebras成績證明/'
attachments = sorted(os.listdir(attachePath))  # 取得成績證明資料夾的所有檔案
#attachments = [attachePath+name for name in os.listdir(attachePath)]


def main():
    # html 格式的信件內容
    htmlcontent = """
    <!doctype html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>HTML mail</title>
    </head>
    <body>
    <b>運算思維挑戰賽挑戰證明</b>
    </body>
    </html>
    """

    # 讀取所有的挑戰證明檔案
    for filename in attachments:
        # 建立郵件主題
        content = MIMEMultipart()  # 建立MIMEMultipart物件
        content["subject"] = subject  # 郵件標題
        content["from"] = from_addr  # 寄件者
        to_addr[0] = filename.split('.')[0] + to_domain  # 收件者 email
        content["to"] = to_addr[0]  # 收件者

        content.attach(MIMEText(htmlcontent, 'html'))

        try:
            with open(attachePath+filename, 'rb') as fp:
                print('讀取 filename=', fp.name)
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())

            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment',
                           filename=os.path.basename(filename))
            content.attach(msg)

        except:
            print("Unable to open one of the attachments. Error: ",
                  sys.exc_info()[0])
            raise

        # 寄送EMAIL
        smtpssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtpssl.login(from_addr, app_passwd)
        print('sendmail from', from_addr, 'to', to_addr, end="")
        status = smtpssl.sendmail(from_addr, to_addr, content.as_string())
        smtpssl.quit()
        if status == {}:
            print(' --- 郵件傳送成功!')
        else:
            print(' --- 失敗', status)


if __name__ == '__main__':
    main()
