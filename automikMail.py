#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import sys
import smtplib
import csv
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import formataddr

EMAIL_HTML_TEMPLATE="""<html>
    <head>
    </head>
    <body>
        <p style ="margin: 5px 0;line-height: 25px;">{},<br>
             <br>
            {}
            <br>
            {}
            <br>
            {}
            <br>
        </p>
    </body>
</html>
"""


class EmailSenderClass:

    #SetUp mail account
    def __init__(self):
        """ """
        self.logaddr = # login
        self.fromaddr = # alias
        self.password = # password


    def sendMessageViaServer(self,toaddr,msg):
        # Send the message via local SMTP server.
        server = smtplib.SMTP('ssl0.ovh.net', 587)
        server.starttls()
        server.login(self.logaddr, self.password)
        text = msg.as_string()
        server.sendmail(self.fromaddr, toaddr, text)
        server.quit()



    def sendHtmlEmailTo(self,destName,destinationAddress,msgBody):
        #Message setup
        msg = MIMEMultipart()
        cc = ["test@gmail.com"]
        recipient = [destinationAddress,
                     "test1@live.fr",
                     "test2@gmail.com"]
        msg['From'] =  "Admin<"+self.fromaddr+">"
        msg['To'] = destinationAddress
        msg['Cc'] = ",".join(cc)
        msg['Subject'] = "Test Object"
        hostname=sys.platform
        #Add text to message
        msg.attach(MIMEText(msgBody, 'html'))

        print("Send email from {} to {}".format(self.fromaddr, destinationAddress))
        self.sendMessageViaServer(recipient, msg)

'''
CSV File (exemple):

Name Surname, mail@engit.fr, redirectionmail@engit.fr
'''


def csvParser(email, file):
    with open(file, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',')
        for info in csvReader:
            if info == []:
                continue
            tmpMessage = EMAIL_HTML_TEMPLATE.format(info[0].split(" ")[0],
                                                    info[1].split("@")[0],
                                                    info[2])
            email.sendHtmlEmailTo(info[0], info[2], tmpMessage)
            tmpMessage = ""
            time.sleep(2)

if __name__ == "__main__":
    email= EmailSenderClass()
    csvParser(email, sys.argv[1])
