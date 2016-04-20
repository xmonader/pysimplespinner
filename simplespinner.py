import time
import threading
from itertools import cycle

class Spinner:
    def __init__(self, sequence=['|', '/', '-', '\\']):
        self.seq=sequence
        self.c=cycle(sequence)
        self.shouldstop=False
        
    def start(self):
        while not self.shouldstop:
            print(next(self.c)+"\b", end='')
                        
    def stop(self):
        self.shouldstop=True


if __name__ == "__main__":
     def heavycomp():
         sp=Spinner()
         threading._start_new_thread(sp.start, ())
         print("please wait...")
         time.sleep(5)
         sp.stop()
         print("we are done")
    

    
