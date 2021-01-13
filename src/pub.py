class Pub:
    
    def __init__(self, name, till, drinks_collection):
        self.name = name
        self.till = till
        self.drink_collection = drinks_collection

    def sell_drink(self,customer,drink):
        if self.check_age(customer):
            customer.buy_drink(drink)
            self.till += drink.price
            return "Customer up to legal age. Drinks served"
        else:
            return "Customer not old enough to drink"


    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    
    # def __init__(self, name,total_cash):
    #     self.name = name
    #     self.total_cash = total_cash