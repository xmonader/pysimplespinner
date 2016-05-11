import time
import threading
from threading import Timer, Thread
from itertools import cycle

class Spinner:
    def __init__(self, interval=0.7, sequence=['|', '/', '-', '\\']):
        self.seq=sequence
        self.c=cycle(sequence)
        self.shouldstop=False
        self.interval=interval

    def start(self):
        while not self.shouldstop:
            time.sleep(self.interval)
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
