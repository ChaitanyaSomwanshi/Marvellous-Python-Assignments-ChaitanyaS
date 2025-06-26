'''
4. Design automation script which accept directory name and mail id from user and create log file in that directory
which contains information of running processes as its name, pid, username. after creating log file send that log
file to the specified mail.

usage : ProcInfoLog.py Demo Chaitanya.somwanshi1392@gmail.com

Demo is name of Directory.
Chaitanya.somwanshi1392@gmail.com is the mail id.

'''

import os
from dotenv import load_dotenv
import psutil
import  datetime
import time
import smtplib as sp
from email.message import EmailMessage

load_dotenv()

def CheckDirectory(DName):

    flag = os.path.isabs(DName)

    if (flag == False):
        DName = os.path.abspath(DName)

    flag = os.path.isdir(DName)

    if (flag == False):
        os.mkdir(DName)

    flag = os.path.exists(DName)

    if (flag == False):
        print("Invalid Path")
        exit()

    print("Absolute path is :", DName)

    Running_Process(DName)


def Running_Process(DName):

    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ['name', 'pid', 'username'])
        info['vms'] = proc.memory_info().vms / (1024 * 1024)
        listprocess.append(info)

    #print(listprocess)
    CreateLog(DName,listprocess)

def CreateLog(DName,listprocess):

    FileCreatedTime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    Fname = "LogFile"+"_"+FileCreatedTime
    FilePath = os.path.join(DName,Fname)

    fobj = open(FilePath,"w")

    border = "-"*80

    fobj.write(border + "\n")
    fobj.write("\t\t Marvellous Info \n")
    fobj.write("\t File Created at :" + time.ctime() + "\n")
    fobj.write(border + "\n")

    for value in listprocess:
        fobj.write(f"{value}  \n")

    fobj.write(border + "\n")


    SendMail(FilePath)


def SendMail(Attachment):

    ob = sp.SMTP('smtp.gmail.com',587)
    ob.ehlo()
    ob.starttls()

    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = os.getenv("RecMailId")

    msg = EmailMessage()

    msg['Subject'] = "Running process file attachment"
    msg['From'] = email_sender
    msg['To'] = email_receiver
    body = "Running process file"
    msg.set_content(body)

    fobj = open(Attachment,"rb")

    fread = fobj.read()

    FileName = os.path.basename(Attachment)

    msg.add_attachment(fread,maintype='application', subtype='octet-stream', filename=FileName)

    ob.login(email_sender,email_password)

    ob.send_message(msg)


def main():

    CheckDirectory(os.getenv("DirName"))

if __name__ == "__main__":
    main()
