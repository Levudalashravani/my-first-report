class VirtualDevice:
    def _init_(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF")

# Example usage
my_device = VirtualDevice("Light Bulb")
my_device.turn_on()
my_device.turn_off()
