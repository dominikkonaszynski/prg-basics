class Phone():
    def __init__(self,battery_level,screen_status,storage_available):
        self.battery_level = battery_level
        self.screen_status = screen_status
        self.storage_available = storage_available

    def charge(self,amount):
        if self.battery_level + amount > 100:
           self.battery_level = 100
        else:
            self.battery_level += amount
        print(f'Charging..., battery level is now {self.battery_level} %')

    def turn_on_off_screen(self):
        self.screen_status = not self.screen_status
        status = "on" if self.screen_status else "off"
        print(f"Screen is now {status}.")
    
    def install_app(self, app_size):
        if self.storage_available >= app_size:
            self.storage_available -= app_size
            print(f"Installing app... {app_size}GB used. Storage left: {self.storage_available}GB.")
        else:
            print("Not enough storage to install the app.")
    
    def display_properties(self):
        screen = "on" if self.screen_status else "off"
        print(f"Battery level: {self.battery_level}%")
        print(f"Screen status: {screen}")
        print(f"Available storage: {self.storage_available} GB")

def main():
    my_phone = Phone(50,False,300)
    my_phone.charge(30)
    my_phone.install_app(175)
    my_phone.turn_on_off_screen()
    my_phone.display_properties()

if __name__ == "__main__":
    main()