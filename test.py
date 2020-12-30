import os, sys, smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


COMMASPACE = ', '
subject = '高師大附中 109學年度國際運算思維挑戰賽 挑戰證明'
from_addr = "mailer@zerojudge.tw"
app_passwd = "zridfkvaolgtoekp"
to_addr = [""]
# 檔案位置 在windows底下記得要加上r 如下 要完整的路徑
attachePath = 'C:\\Users\\user\\Downloads\\grades-高一忠\\'
attachments = os.listdir(attachePath)
#attachments = [attachePath+name for name in os.listdir(attachePath)]

def main():
    # sender = '你的EMAIL'
    # gmail_password = '你的EMAIL密碼'
    # recipients = ['收件人01的EMAIL','收件人02的EMAIL']
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

    # 加入檔案到MAIL底下
    for filename in attachments:
        # 建立郵件主題
        content = MIMEMultipart()  #建立MIMEMultipart物件
        content["subject"] = subject  #郵件標題
        content["from"] = from_addr  #寄件者

        content.attach(MIMEText(htmlcontent, 'html'))
        to_addr[0] = filename.split('.')[0]+'@gmail.com'
        content["to"] = to_addr[0] #收件者

        try:
            with open(attachePath+filename, 'rb') as fp:
                print('can read faile filename=',filename, 'fp=', fp)
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
            print(' ---', status)


if __name__ == '__main__':
    main()
