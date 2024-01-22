from threading import*
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2) #to avoid collision
t2.start()

t1.join() #asking main thread to wait for t1
t2.join()  #asking main thread to wait for t2
print("Bye")