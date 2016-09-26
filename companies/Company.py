__author__ = 'ajitkumar'
from transaction.TransactionQueue import TransactionQueue


class Company:
    """
    Class for company
    """
    def __init__(self, name):
        self.name = name
        self.buy_queue = TransactionQueue()
        self.sell_queue = TransactionQueue()

    def return_buy_queue(self):
        return self.buy_queue

    def return_sell_queue(self):
        return self.sell_queue

    def __str__(self):
        value = "name = {0}, buy_queue = {1}, sell_queue = {2}".format(
            self.name,
            self.buy_queue,
            self.sell_queue
        )
        return value

    def __repr__(self):
        return "name = {0}, buy_queue = {1}, sell_queue = {2}".format(
            self.name,
            self.buy_queue,
            self.sell_queue
        )



