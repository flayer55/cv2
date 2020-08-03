import threading
from time import *
def Timer(timing):
    print('sleeping...')

    sleep(timing)

def Action():
    for i in range(1000):
        print("hello", threading.current_thread().name)

# thread = threading.Thread(target= Timer(80))
act_thread = threading.Thread(target= Action)
act_thread.start()
Timer(80)