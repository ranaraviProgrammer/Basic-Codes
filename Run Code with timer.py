import sys
import schedule
import time

def show_message():
    print("Run! ", end='', flush=True)
    
schedule.every(2).seconds.do(show_message)

while(1):
    schedule.run_pending()
    time.sleep(1)
