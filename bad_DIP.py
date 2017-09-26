"""
bad example of Dependency Inversion of SOLID principles
High level ElectricPowerSwitch class is directly dependent on low level
LightBulb class. LightBulb class is hardcoded in ElectricPowerSwitch.
But a switch shouldn't be tight to bulb. It should be turn on and off other appliances too
like fan, ac. To achieve this, we need to modify ElectricPowerSwitch each time.
"""


class LightBulb(object):
    def turn_on(self):
        print "LightBulb: Bulb turned on.."

    def turn_off(self):
        print "LightBulb: Bulb turned off.."


class ElectricPowerSwitch(object):

    def __init__(self, light_bulb):
        self.light_bulb = light_bulb
        self.on = False

    def is_on(self):
        return self.on

    def press(self):
        check_on = self.is_on()
        if (check_on):
            self.light_bulb.turn_on()
            self.on = False
        else:
            self.light_bulb.turn_off()
            self.on = True


def main():
    light_bulb = LightBulb()
    electric_switch = ElectricPowerSwitch(light_bulb)
    electric_switch.press()
    electric_switch.press()
    electric_switch.press()

if __name__ == '__main__':
    main()
