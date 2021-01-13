import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("shots", 10, 7)
        self.drink2 = Drink("spirits", 10, 5)
        drinks = [self.drink1, self.drink2]
        self.pub = Pub("ponies",  0, drinks)
        self.customer = Customer("Johnny Bravo", 50, 23)
        
    def test_buy_drink(self):
        self.customer.buy_drink(self.drink1)
        self.assertEqual(40, self.customer.wallet)
        self.assertEqual(7, self.customer.drunkenness)
      

    


