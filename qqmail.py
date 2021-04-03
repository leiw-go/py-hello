import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="leiwsnc@qq.com"    #用户名
mail_pass="pdcuulypcwusfcch"   #口令 
 
sender = 'leiwsnc@qq.com'
receivers = ['1766318380@qq.com',"1143919710@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#创建实例
message = MIMEMultipart()
message['From'] = Header("leiw", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = '功能整合，一键测试'
message['Subject'] = Header(subject, 'utf-8')
message.attach(MIMEText('你好，请查收本次抓取结果', 'plain', 'utf-8'))
#附件
att1 = MIMEText(open('sourcecatch.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写
att1["Content-Disposition"] = 'attachment; filename="sourcecatch.txt"'
message.attach(att1)
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("Send successfully!")
except smtplib.SMTPException:
    print ("Error: something wrong")