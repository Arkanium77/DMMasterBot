import os
import time

while (True):
    try:
        os.system("python main.py")
        print("start again")
    except Exception:
        time.sleep(100)
    time.sleep(300)