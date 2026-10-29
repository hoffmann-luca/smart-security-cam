import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email import Encoders
user = '' #mail
pwd = '' #mail password
def sendMail(to,subject,text, image):
    msg = MIMEMultipart('related')
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    msgText = MIMEText(text)
    msg.attach(msgText)

    fp = open(image, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print "[+] Connecting To Mail Server."
        smtpServer.ehlo()
        print "[+] Starting Encrypted Session."
        smtpServer.starttls()
        smtpServer.ehlo()
        print "[+] Logging Into Mail Server."
        smtpServer.login(user,pwd)
        print "[+] Sending Mail."
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print "[+] Mail Sent Successfully.\n"
    except:
        print "[-] Sending Mail Failed."
