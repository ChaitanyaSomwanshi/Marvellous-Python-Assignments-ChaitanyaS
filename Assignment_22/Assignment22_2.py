'''

2. Design automation script which accept process names and display information of that process if it is running.

Usage : ProcInfoLog.py Notepad

'''

import psutil

def CheckProcess(Name):

    listprocess = []

    for proc in psutil.process_iter():
        if Name == proc.name():
            info = proc.as_dict(attrs = ['pid','username','name'])
            listprocess.append(info)

    print(listprocess)


def main():

    CheckProcess('Notepad.exe')






if __name__ == "__main__":
    main()