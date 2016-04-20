import time
import threading
from threading import Timer, Thread
from itertools import cycle

class Spinner:
    def __init__(self, sequence=['|', '/', '-', '\\']):
        self.seq=sequence
        self.c=cycle(sequence)
        self.shouldstop=False
        
    def start(self):
        while not self.shouldstop:
            time.sleep(0.07)
            print("\r"+next(self.c), end='')
                        
    def stop(self):
        self.shouldstop=True
        print("\r")
        
    def __enter__(self):
        threading._start_new_thread(self.start, ())
        
    def __exit__(self, *args):
        self.stop()

         


if __name__ == "__main__":
    with Spinner():
        print("Long computation")
        time.sleep(5)
    print("Done")