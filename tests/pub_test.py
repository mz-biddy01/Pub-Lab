import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("shots", 10, 7)
        self.drink2 = Drink("spirits", 20, 5)
        self.drinks_collection = [self.drink1, self.drink2]
        self.pub = Pub("The Goose", 190, self.drinks_collection)
        self.customer = Customer("Johnny Bravo", 50, 23)

    def test_sell_drink_increases_till_amount(self):
        self.pub.sell_drink(self.customer, self.drink2)
        self.assertEqual(210, self.pub.till)



    
    # def setUp(self):
    #     self.pub = Pub("The Prancing Pony", 100.00)

    # def test_pub_has_name(self):
    #     self.assertEqual("The Prancing Pony", self.pub.name)