'''
1. Write a Python script that prints "Jay Ganesh..." every 2 seconds. Use the schedule.every(2).seconds.do(...)
function.

'''

import schedule
import time
import datetime


def JayGanesh():
    print(f"Jay Ganesh :  {datetime.datetime.now()}")
    


def main():

    schedule.every(2).seconds.do(JayGanesh)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()