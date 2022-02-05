class Vehicle():
    def __init__(self, vtype, mileage, fuel_left, initial_fuel):
        self.vtype = vtype
        self.mileage = mileage
        self.fuel_left = fuel_left
        self.initial_fuel = initial_fuel

    def distance_can_be_travelled(self):
        if self.fuel_left <= 5:
            return 0
        else:
            return (self.fuel_left-5)*self.mileage

    def distance_travelled(self):
        distance_travelled = (self.initial_fuel - self.fuel_left)*self.mileage
        return distance_travelled


car1 = Vehicle("car", 18, 5, 8)
print("distance can be travelled", car1.distance_can_be_travelled())
print("distance travelled till now is", car1.distance_travelled())
