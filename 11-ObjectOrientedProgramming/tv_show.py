from tv import TV
def main():
    tv1 = TV()
    tv1.show_status()
    tv1.turn_on()
    tv1.show_status()
    tv1.show_channels()
    tv1.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    tv1.show_channels()
    tv1.set_channel(1)
    tv1.increase_volume(3)
    tv1.show_status()
    tv1.turn_off()
    
if __name__ == "__main__":
    main()