from time import *
import threading
delay = 60
del_thread = threading.Thread(target= sleep(delay))
def Thread(func):
    def Wrapper(*args, **kwargs):
        current_thread = threading.Thread(target= func, args= args, kwargs= kwargs)
        current_thread.start()
    return Wrapper

start = time()
@Thread
def Timer(timing):
   sleep(timing)

# end = time()
# print(end - start)

print(Timer(60))
while True:
    print("Hello geek")
