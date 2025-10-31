from Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, model, rentalrate, hours):
        super().__init__(model, rentalrate)
        self.hours = hours

    def cal_rentalrate(self):
        truckrentalrate = self.rentalrate * self.hours
        return truckrentalrate

