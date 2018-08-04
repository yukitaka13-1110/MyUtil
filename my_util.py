import time


class Measure:

    def __init__(self):
        self._start = 0
        self._stop = 0

    def start(self):
        self._start = time.time()

    def stop(self, process):
        self._stop = time.time()
        print(process+" End : ",str(self._stop-self._start))
