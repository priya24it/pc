import logging
import inspect
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

class Commonclass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log','w+')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        #fileHandler.close()
        return logger

    def send_status(self, logfile):
        email_user = 'priya12it'
        email_password = 'Criminal@12'
        email = 'priya12it@gmail.com'
        today = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
        subject = 'Test execution status: ' + today
        print("inside send_status")
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email
        msg['Subject'] = subject
        body = 'Dear Priya,' + '\n\n' + 'Attached is the log file.' '\n\n' + 'Thanks,' + '\n''xa'
        print("After body")
        msg.attach(MIMEText(body, 'plain'))
        filename = logfile
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        attach_name = 'Avaya_outfile.PDF'
        part.add_header('Content-Disposition', "attachment; filename= " + attach_name)
        msg.attach(part)
        text = msg.as_string()
        print("before accessing outlook server")

        mailserver = smtplib.SMTP(host='smtp.gmail.com', port=25)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(email_user, email_password)
        mailserver.sendmail(email_user, email, text)
        mailserver.quit()
