'''

8. Write a script that simulates checking for email updates every 10 seconds.(use a print statement like " 
Checking mail..." insted of real email logic.)

'''


import schedule
import time



def checking_mail():


    print("Checking mail...")


def main():
    schedule.every(10).seconds.do(checking_mail)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()