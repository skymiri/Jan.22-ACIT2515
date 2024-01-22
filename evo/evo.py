class Evo:
    def __init__(self):
        self.driver = None
        self.distance = 0

    def start_rental(self, driver):

        if self.driver is not None:
            raise RuntimeError("Cannot start a rental without a driver")

        self.driver = driver
        print(f"{self.driver} is starting a rental")

    def drive(self, distance):

        if self.driver is not None:
            raise RuntimeError("Cannot start a rental without a driver")

        if distance < 0:
            raise AttributeError(
                "The distance driven must be a positive number")

        self.distance += distance
        print(f"{self.driver} is driving {self.distance} km")
        # if no rider is defined on the bike, raise a  RuntimeError
        # if self.driver is None:

    def end_rental(self):

        if self.driver is not None:
            raise RuntimeError("Cannot end a rental without a driver")

        driven_distance = self.distance
        self.driver = None
        self.distance = 0
        print(f"{self.driver} is ending a rental")

        return driven_distance
