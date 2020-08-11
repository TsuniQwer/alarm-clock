# alarm-clock
wake up!


import time
import os
import threading


class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW!")
                    os.popen("run.mp3")
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False



name = input("Enter your name: ")

print("Hello, " + name)

alarm_HH = input("Enter the hour you want to wake up at: ")
alarm_MM = input("Enter the minute you want to wake up at: ")



alarm = Alarm(alarm_HH, alarm_MM)
alarm.start()

try:
    while True:
         text = str(input("stop: "))
         if text == "stop":
            alarm.just_die()
            break
except:
    print("Yikes lets get out of here")
    alarm.just_die()
