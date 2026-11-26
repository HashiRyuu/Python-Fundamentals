from car import Car

class Limousine(Car):
    def __init__(self):
        super().__init__()
        super().setNumberOfTires(8)
