import time
class Timer:

    def __enter__(self):
        self.start = time.time()
        print("Timer Started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print(f"Elapsed Time: {end - self.start:.6f} seconds")


with Timer():
    for i in range(1000000):
        pass