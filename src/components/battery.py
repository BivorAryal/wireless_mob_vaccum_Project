class BatterySensor:
    def __init__(self):
        self.level = 100  # Starting at full battery

    def get_level(self):
        # Decrease battery level over time for simulation
        self.level -= 1
        return self.level