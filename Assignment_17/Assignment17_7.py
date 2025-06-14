'''

7. Schedule a function that performs file backup every hour and write a log entry into backup_log.txt


'''

import schedule
import time
import datetime




def Backup_Log():
    
    Lfile = open("backup_log.txt","a")

    Lfile.write(f"last Backup date & time : {datetime.datetime.now()}\n")


def main():

    schedule.every(1).minute.do(Backup_Log)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()