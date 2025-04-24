# 104. Schedule a function to run every n seconds.
import schedule
import time
def greetings():
    print("Hello dear good morning !")

# schedule.every(3).seconds.do(greetings())

schedule.every(3).seconds.do(greetings)
for _ in range(0,10):
    print('nice')
    time.sleep(1)
while True:
    schedule.run_pending()
    # time.sleep(1)

    