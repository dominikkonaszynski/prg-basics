class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 5
    
    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            if self.channels:
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume: {self.volume}")
            else:
                print("TV is on, but no channels are available")   
        else:
            print("TV is off")

    def set_channel(self, new_channel_no):
        if 1 <= new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no
        else:
            print("Invalid channel number. Please select a vaild channel.")
    
    def set_channels(self,channels_list):
        self.channels = channels_list

    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for i,channel in enumerate(self.channels, 1):
                print(f"{i}. {channel}")
        else:
            print("No channels available")

    def increase_volume(self, amount):
        if self.volume + amount > 10:
            self.volume = 10
            print("Volume is at maximum (10)")
        else:
            self.volume += amount
            print(f"Volume increased to {self.volume}.")
    
    def decrease_volume(self,amount):
        if self.volume - amount < 0:
            self.volume = 0
            print("Volume is at minimum (0)")
        else:
            self.volume -= amount
            print(f"Volume decreased to {self.volume}.")