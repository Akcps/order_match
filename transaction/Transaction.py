__author__ = 'ajitkumar'


class Transaction:
    """
    Class for each transaction - buy/sell
    """
    def __init__(self,
                 order_number,
                 transaction_type,
                 price,
                 timestamp,
                 no_of_stocks):
        self.order_number = order_number
        self.transaction_type = transaction_type
        self.price = price
        self.timestamp = timestamp
        self.no_of_stocks = no_of_stocks

    def __str__(self):
        return "[order_number = {0}, transaction_type = {1}, price = {2}, timestamp = {3}, no_of_stocks = {4}]".format(
            self.order_number,
            self.transaction_type,
            self.price,
            self.timestamp,
            self.no_of_stocks
        )

    def __repr__(self):
        return "[order_number = {0}, transaction_type = {1}, price = {2}, timestamp = {3}, no_of_stocks = {4}]".format(
            self.order_number,
            self.transaction_type,
            self.price,
            self.timestamp,
            self.no_of_stocks
        )



