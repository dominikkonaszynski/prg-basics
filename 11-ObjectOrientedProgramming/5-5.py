import random
class Thermometer():
    def __init__(self):
        self.is_on = False
        self.temperature_rounded = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        self.temperature_rounded = round(random.uniform(34, 42), 1)
        print("Measuring...")
        
    def display(self):
        if self.is_on:
            if self.temperature_rounded >= 37 and self.temperature_rounded < 41:
                print(f"Temperature: {self.temperature_rounded}C (fever)")
            elif self.temperature_rounded >= 41: 
                print(f"Temperature: {self.temperature_rounded}C (CRITICAL TEMPERATURE!!)")
            else:
                print(f"Temperature: {self.temperature_rounded}C (normal)")
        else:
            print("Turn the thermometer on")
    
def main():
    therm1 = Thermometer()
    therm1.turn_on()
    therm1.measure()
    therm1.display()
    therm1.turn_off()

if __name__ == "__main__":
    main()