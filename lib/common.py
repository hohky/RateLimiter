import time
import sys
from colorama import init
from colorama import Fore as c

init()

"""
def animation_wait(message):
    animation = "|/-\\"
    #start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            anime = animation[i % len(animation)]
            print(f"[{c.LIGHTGREEN_EX}{anime}{c.RESET}] {message}", end="\r")
            #sys.stdout.write("\r" + animation[i % len(animation)])
            #sys.stdout.flush()
        #if time.time() - start_time > 10:  # The animation will last for 10 seconds
            #break

"""
"""
def animation_wait(message, duration=10):
    animation = "|/-\\"
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(len(animation)):
            time.sleep(0.2)
            anime = animation[i % len(animation)]
            print(f"[{c.LIGHTGREEN_EX}{anime}{c.RESET}] {message}", end="\r")
            if time.time() - start_time >= duration:
                break
"""