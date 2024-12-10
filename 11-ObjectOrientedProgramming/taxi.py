class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'{self.distance} km, {self.rate_per_km} zl, {self.fare} zl')


def main():
    ride1 = TaxiRide(2)
    ride2 = TaxiRide(3)
    ride1.calculate_fare(10)
    ride2.calculate_fare(15)
    print('Details of the ride 1:')
    ride1.print_receipt()
    print(f'Details of the ride 2:')
    ride2.print_receipt()

if __name__ == "__main__":
    main()
