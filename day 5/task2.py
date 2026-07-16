class Counter:
    total_objects = 0

    def __init__(self):
        Counter.total_objects += 1

    @classmethod
    def get_count(cls):
        return cls.total_objects


c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()

print("Total Counter Objects:", Counter.get_count())
