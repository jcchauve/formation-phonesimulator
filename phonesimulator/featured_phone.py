# coding: utf8
"""classe de telephone basique"""

try:
    from phone import Phone
except:
    from .phone import Phone

class FeaturedPhone(Phone):
    """phonte"""
    def reset(self):
        self.battery_level = 40

    def __init__(self):
        super(FeaturedPhone, self).__init__()
        self.reset()

    def workfor(self, seconds):
        self.battery_level -= seconds / 60
        if self.battery_level < 0:
            self.battery_level = 0

    def chargefor(self, seconds):
        self.battery_level += seconds / 30
        if self.battery_level > 100:
            self.battery_level = 100
