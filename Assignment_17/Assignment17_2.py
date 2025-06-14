'''
2. Schedule a task that displays the cureent date and time every minute using the datetime module.

'''

import datetime
import schedule
import time


def display():

    print("Current date time is :", datetime.datetime.now())

def main():

    schedule.every(1).minute.do(display)


    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()

    