import unittest
from phonesimulator.featured_phone import FeaturedPhone


class factPhone(unittest.TestCase):
    def setUp(self):
        self.phone = FeaturedPhone()

    def reset(self):
        self.phone.reset()

    def test_workfor(self):
        self.reset()
        self.phone.workfor(60)
        self.assertEqual(self.phone.battery_level, 39)

    def test_workfor_long(self):
        self.reset()
        self.phone.workfor(6000000)
        self.assertEqual(self.phone.battery_level, 0)

    def test_chargefor(self):
        self.reset()
        self.phone.chargefor(60)
        self.assertEqual(self.phone.battery_level, 42)

    def test_chargefor_long(self):
        self.reset()
        self.phone.chargefor(600000000)
        self.assertEqual(self.phone.battery_level, 100)


if __name__ == '__main__':
    unittest.main()
