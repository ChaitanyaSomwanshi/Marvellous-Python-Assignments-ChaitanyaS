'''
3. Design automation script which accept directory name from user and create log file in that directory which
contains information of running processes as its name, PID, username.

Usage : ProcInfoLog.py Demo

Demo is name of Directory.
'''

import os
import psutil
import datetime
import time

def CheckDirectory(DirName):

    

    flag = os.path.isabs(DirName)


    if (flag == False):
        DirName = os.path.abspath(DirName)


    flag = os.path.isdir(DirName)

    if (flag == False):
        os.mkdir(DirName)

    flag = os.path.exists(DirName)

    if (flag == False):
        print("Invalid Path")
        exit()

    # print("AbsolutePath is :", DirName)

    Running_Process(DirName)


def Running_Process(DirName):

    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ['name', 'pid', 'username'])
        info['vms'] = proc.memory_info().vms / (1024 * 1024)
        listprocess.append(info)

    
    # print(listprocess)
    CreateLog(DirName,listprocess)


def CreateLog(DirName,listprocess):

    FileCreateTime = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S")
    FileName = "RunningProcessLogFile" +"_"+ FileCreateTime
    FilePath = os.path.join(DirName,FileName)

    print(FileName)

    fobj = open(FilePath,"w")

    border = "-"*80

    fobj.write(border +"\n")
    fobj.write("\t\tMarvellous InfoSystem process log \n")
    fobj.write("\t\tLog file is Created at : " +time.ctime()+"\n")
    fobj.write(border +"\n")

    for value in listprocess:
        fobj.write(f"{value} \n")

    fobj.write(border +"\n")

    

def main():

    CheckDirectory("Demo")


if __name__ == "__main__":
    main()