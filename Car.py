from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, model, rentalrate, hours):
        super().__init__(model, rentalrate)
        self.hours = hours

    def cal_rentalrate(self):
        carrentalrate = self.rentalrate * self.hours
        return carrentalrate
