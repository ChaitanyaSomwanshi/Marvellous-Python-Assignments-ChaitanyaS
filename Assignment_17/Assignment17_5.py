'''

5. Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt.

'''
import schedule
import time
import datetime

def Marvellous():

    Mfile = open("Marvellous.txt","a")

    Mfile.write(f"Current Date and Time : {datetime.datetime.now()}\n")


def main():

    schedule.every(5).minutes.do(Marvellous)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

