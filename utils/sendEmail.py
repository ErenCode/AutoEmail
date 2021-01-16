
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import datetime
import logging

log = logging.getLogger(__name__)

def send_mail_html(sender,receiver,cc,subject,username,password,filepath,sheetnames,mail_body,log,filename):
    """

    :param sender: email addr to send the emails:string 'xxx@xx.com'
    :param receiver: email addr to receive the emails: list of string ['xxx@xx.com','xxx@xx.com']
    :param cc: email addr to receive the emails transcripts: list of string [''xxx@xx.com'']
    :param subject: the subject of this email: string "运营业务周报"
    :param username: login username: string  r''
    :param password: login password: string ''
    :param filepath: the path of the attached file: string "./weekly/运营业务周报.xlsx"
    :param sheetnames: sheetnames of the excel: list of strings ["",""]
    :param mail_body: html content
    :param log : personalize logger
    :return: string of the result: 邮件发送成功！
    """

    # 发送者邮箱
    sender = sender

    # 接收者的邮箱地址
    receiver = receiver   # receiver 可以是一个list
    #抄送人的邮箱地址
    cc= cc
    start_day = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%Y%m%d')
    end_day = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')

    timePeriod = start_day + '-' + end_day

    # 发送邮件主题
    subject =subject +timePeriod

    # 发送邮箱服务器
    smtpserver = 'ip地址'

    # 发送邮箱用户/密码
    username = username
    password = password

    mail_body=mail_body
    # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    # msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')

    #构建一个带附件的实例
    msg=MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    # msg['From'] =','.join(sender)
    # msg['Cc']=','.join(cc)
    # msg['To'] =','.join(receiver)
    msg['From'] = sender
    msg['Cc']=','.join(cc)
    msg['To'] =','.join(receiver)

    msg.attach(MIMEText(mail_body, _subtype='html', _charset='utf-8'))

    #附件名

    # print('filename:',filename)
    xlsx = MIMEApplication(open(filepath, 'rb').read())
    xlsx["Content-Type"] = 'application/octet-stream'
    xlsx.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(xlsx)

    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP(smtpserver)
        smtp.connect(smtpserver,25)

        #换ssl发送
        # smtp=smtplib.SMTP_SSL(smtpserver,443)
        # smtp=smtplib.SMTP_SSL(smtpserver,25)
        smtp.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
        smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        # print("邮件发送失败！",e)
        log.error("邮件发送失败！"+ str(e))
    else:
        # print("邮件发送成功！")
        # log.info(id + '\t' + '邮件发送成功！')
        log.info("邮件发送成功" + "")
    # finally:
    #     smtp.quit()



if __name__=="__main__":
    pass