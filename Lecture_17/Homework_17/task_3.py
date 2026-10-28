class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

class SmartLight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        if  0.00 <= brightness <= 100:
            self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print(f"Brand: {self.brand}, Brightness is {self.brightness}")


Smartlight1 = SmartLight("Samsung", 80)
Smartlight1.turn_on()
        