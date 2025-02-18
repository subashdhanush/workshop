import time
import datetime

alarm_time = input("Enter alarm time (HH:MM:SS): ")
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Time to Wake Up!")
        break
    time.sleep(1)
