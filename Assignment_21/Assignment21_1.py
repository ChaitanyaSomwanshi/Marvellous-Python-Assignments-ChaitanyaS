'''
Please follow below rules while designing automation script as

● Accept input through command line or through file
● Display any message in log file instead of console
● For Separate task define Separate function
● For robustness handle every exptected exception
● Perform validations before taking any action.
● Create user defined modules to store the functionality.


Design automation script which perform following task.

Accept Directory Name from user and delete all duplicate files from the specified directory by considering the
checksum of files.
Create one Directory named as marvellous and inside that Directory create log file which maintains all names of
duplicate files which are deleted.
Name of that log file should contains the date and time at which that files gets created.
Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
Accept mail id from user and send the attachment of the log file.
Mail body should contains statistics about the operation file removal.

Mail body should contains below things :
    Starting time of scanning
    Total Number of files scanned 
    Total Number of duplicate files found

Consider below command line options for the gives script

DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

-   DuplicateFileRemoval.py : Name of python automation script
-   E:/Data/Demo : Absolute path of directory which may contains duplicate files
-   50 : Time interval of script in minutes
-   marvellousinfosystem@gmail.com : mail ID of the receiver

Note :
for every separate task write separate function.
Write all user defined funtions in one user defined module.
user proper validation techniques
provide help and usage option for script
Create one Readme file which contains description of our script, details of command line options.


'''
import sys
import os
import hashlib
import time
import schedule
import smtplib as sp
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()
import datetime



def CheckDirectory(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        DirName = os.path.abspath(DirName)

    flag = os.path.exists(DirName)

    if (flag == False):
        print("Invalid Path")
        exit()

    flag = os.path.isdir(DirName)

    if (flag == False):
        print("Valid Path but directory not found")
        exit()

    print("Absolute Path is :", DirName)

    Duplicate = {}
    TotalFiles = 0
    StartTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for FolderName, SubFolderNames, FileNames in os.walk(DirName):

        for File in FileNames:
            FName = os.path.join(FolderName,File)
            TotalFiles = TotalFiles + 1
            checksum = Checksum(FName)

            if checksum in Duplicate:
                Duplicate[checksum].append(FName)

            else:
                Duplicate[checksum] = [FName]


    DeleteDuplicate(Duplicate,StartTime,TotalFiles)
    
   


def Checksum(File):

    BlockSize = 1024

    fobj = open(File,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)

    while (len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    
    return hobj.hexdigest()

def DeleteDuplicate(Data,StartTime,TotalFiles):

    result = list(filter(lambda x : len(x) > 1, Data.values()))

    DeleteFiles = []

    count = 0
    cnt = 0

    for value in result:
        for subvalue in value:
            count = count + 1

            if (count > 1):
                cnt = cnt + 1
                DeleteFiles.append(subvalue)
                os.remove(subvalue)

        count = 0

    
    makeDir("Marvellous",DeleteFiles,StartTime,TotalFiles,len(DeleteFiles))

def makeDir(Name,Data,StartTime,TotalFiles,DuplicateFiles):

    flag = os.path.isdir(Name)

    if (flag == False):
        os.mkdir(Name)

    LogfileName = "DeletedFile" + time.ctime() +".txt"

    LogfileName = LogfileName.replace(":","_")

    LogfilePath = os.path.join(Name,LogfileName)

    fobj = open(LogfilePath,"a")

    fobj.write("-" * 84 + "\n")
    fobj.write(f"File created at : {time.ctime()} \n")
    fobj.write("-" * 84 + "\n")
    fobj.write(f"ScanStartTime : {StartTime} \n")
    fobj.write(f"TotalScanned : {TotalFiles} \n")
    fobj.write(f"DuplicateFiles : {DuplicateFiles} \n")
    fobj.write("-" * 84 + "\n")

    for i in Data:

        FileName = i.rsplit("\\",1)[1]
        fobj.write(f"{FileName} \n")
    
    fobj.write("-" * 84 + "\n")
    fobj.close()
    SendMail(LogfilePath)


def SendMail(LogfilePath):

    ob = sp.SMTP('smtp.gmail.com',587)
    ob.ehlo()
    ob.starttls()

    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = os.getenv("EMAIL_RECEIVER")

    msg = EmailMessage()
    msg['Subject'] = "Duplicate file Attachmnet"
    msg['From'] = email_sender
    msg['To'] = email_receiver
    body = "Duplicate File Attached"
    msg.set_content(body)

    
    fobj = open(LogfilePath,'rb')

    FileData = fobj.read()
    file_name = os.path.basename(LogfilePath)

    msg.add_attachment(FileData,maintype='application', subtype='octet-stream', filename=file_name)


    ob.login(email_sender,email_password)

    ob.send_message(msg)





def main():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is automation script for delete duplicate files.")
            exit()

        if (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Plaese provide arguments as mention below :")
            print("◉ DuplicateFileRemoval.py : Name of python automation script")
            print("◉ E:/Data/Demo : Absolute path of directory which may contains duplicate files")
            print("◉ 50 : Time interval of script in minutes")
            print("◉ marvellousinfosystem@gmail.com : mail ID of the receiver")
            exit()


    if (len(sys.argv) != 5):
        print("Invalid Arguments, please use '--h' for help and '--u' for usage")

    else:

        # CheckDirectory(sys.argv[1])

        schedule.every(int(os.getenv("ScheduleTime"))).minutes.do(CheckDirectory,sys.argv[1])


        while True:
            schedule.run_pending()

            time.sleep(1)




if __name__ == "__main__":
    main()
