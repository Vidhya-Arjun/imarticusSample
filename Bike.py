from Vehicle import Vehicle
class Bike(Vehicle):
    def __init__(self,model,rentalrate,hours):
        super().__init__(model,rentalrate)
        self.hours = hours
    def cal_rentalrate(self):
        bikerentalrate = self.rentalrate * self.hours
        return bikerentalrate
