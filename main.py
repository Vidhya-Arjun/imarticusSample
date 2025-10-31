from Bike import Bike
from Car import Car
from Truck import Truck

if __name__ == '__main__':
    bik = Bike("rm5",200,2)
    car = Car("Ford",500,7)
    truck = Truck("Mahendra",100,6)

vehicle = [bik, car, truck]
for v in vehicle:
    print(v)