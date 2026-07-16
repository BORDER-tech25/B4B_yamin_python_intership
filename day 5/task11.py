class Bird:
    def fly(self):
        print("Bird is flying.")


class Airplane:
    def fly(self):
        print("Airplane is flying.")


class Drone:
    def fly(self):
        print("Drone is flying.")


def start_flying(obj):
    obj.fly()


bird = Bird()
plane = Airplane()
drone = Drone()

start_flying(bird)
start_flying(plane)
start_flying(drone)
