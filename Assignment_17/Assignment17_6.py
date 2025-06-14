'''
6. Write a script that schedules multiple task: one to print "lunch time!" at 1 PM, and another to print
"Wrap up work" at 6 PM.

'''



import schedule
import datetime
import time

def lunch():

    print("lunch time!")


def Wrap():

    print("Wrap up work")



def main():

    schedule.every().day.at("12:22").do(lunch)

    schedule.every().day.at("12:25").do(Wrap)


    while True:
        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()
