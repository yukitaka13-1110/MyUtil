import time


class Measure:

    def __init__(self):
        self._start = {}
        self._stop = {}

    def start(self, process):
        self._start[process] = time.time()

    def stop(self, process):
        if process not in self._start:
            print("Measure: No such process '%s'"%process)
            return
        self._stop[process] = time.time()

    def time(self, process):
        if process not in self._start or process not in self._stop:
            print("Measure: No such process '%s'"%process)
            return
        print("Time of %s ==> "%process,self._stop[process]-self._start[process])


def main():
    pass


if __name__ == '__main__':
    main()
