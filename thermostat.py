class Thermostat:
    def _init_(self, target_temp, current_temp):
        self.target_temp = target_temp
        self.current_temp = current_temp

    def increase_temp(self, degrees):
        self.target_temp += degrees
        print(f"Target temperature increased to {self.target_temp}°C")

    def decrease_temp(self, degrees):
        self.target_temp -= degrees
        print(f"Target temperature decreased to {self.target_temp}°C")

    def display_temps(self):
        print(f"Current temperature: {self.current_temp}°C")
        print(f"Target temperature: {self.target_temp}°C")

# Example usage
my_thermostat = Thermostat(20, 22)
my_thermostat.display_temps()
my_thermostat.increase_temp(2)
my_thermostat.display_temps()
