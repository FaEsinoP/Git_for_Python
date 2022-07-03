class Car:
    def __init__(self, everage, h, w):
        self.everage_speed = everage
        self.height = h
        self.weight = w

    def start_engine(self):
        print("RrrRRRrRRrr!")

    def show_max_speed(self, everage_speed):
        print(f"Max_speed: {everage_speed * 2} км/c")


mustang = Car(1, 1, 1)
mustang.start_engine()
mustang.show_max_speed(mustang.everage_speed)
