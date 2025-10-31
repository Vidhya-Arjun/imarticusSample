class Vehicle:
    def __init__(self,model,rentalrate):
        self.model = model
        self.rentalrate = rentalrate
    def cal_rentalrate(self):
        return self.rentalrate
    def __str__(self):
        return f'Model: {self.model}, Rental Rate: {self.cal_rentalrate()}'