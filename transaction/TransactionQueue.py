__author__ = 'ajitkumar'


class TransactionQueue:
    """
    Class for Buy/Sell Queue
    """
    def __init__(self):
        self.transactions = list()
        self.price_set = set()

    def sort_list(self, reverse=False):
        self.transactions = sorted(self.transactions,
                                   key=lambda x:
                                   (x.price, x.timestamp),
                                   reverse=reverse)

    def insert(self, transaction):
        self.transactions.append(transaction)
        if transaction.transaction_type.lower() == "buy":
            self.sort_list(True)
        else:
            self.sort_list()

    def peek(self):
        return self.transactions[0]

    def pop(self):
        top = self.transactions[0]
        del(self.transactions[0])
        return top

    def is_empty(self):
        return True if len(self.transactions) == 0 else False

    def insert_transaction(self, transaction):
        if not self.transactions:
            self.transactions.append(transaction)
            self.price_set.add(transaction.price)
        else:
            if transaction.price not in self.price_set:
                if transaction.transaction_type.lower() == "sell":
                    self.insert_into_sell_queue(transaction)
                else:
                    self.insert_into_buy_queue(transaction)
                self.price_set.add(transaction.price)
            else:
                import pdb;pdb.set_trace()
                if transaction.transaction_type.lower() == "sell":
                    self.insert_into_sell_queue(transaction, True)
                else:
                    self.insert_into_buy_queue(transaction, True)

    def insert_into_sell_queue(self, new_transaction, timestamp=False):
        self.sort_list()
        import pdb;pdb.set_trace()
        new_transaction_list = list()
        i = 0
        for i, transaction in enumerate(self.transactions):
            if new_transaction.price < transaction.price:
                new_transaction_list.append(new_transaction)
            elif new_transaction.price == transaction.price:
                if transaction.timestamp < new_transaction.timestamp:
                    new_transaction_list.append(transaction)
                    new_transaction_list.append(new_transaction)
                else:
                    new_transaction_list.append(new_transaction)
                    new_transaction_list.append(transaction)
            else:
                new_transaction_list.append(transaction)
        if len(self.transactions)-1 == i:
            new_transaction_list.append(new_transaction)
        self.transactions = new_transaction_list

    def insert_into_buy_queue(self, new_transaction, timestamp=False):
        new_transaction_list = list()
        i = 0
        for i, transaction in enumerate(self.transactions):
            if new_transaction.price > transaction.price:
                if not timestamp:
                    new_transaction_list.extend(self.transactions[:i])
                else:
                    new_transaction_list.extend(self.transactions[:i-1])
                    if self.transactions[i].timestamp < new_transaction.timestamp:
                        new_transaction_list.append(self.transactions[i])
                        new_transaction_list.append(new_transaction)
        new_transaction_list.append(new_transaction)
        new_transaction_list.extend(self.transactions[i:])
        self.transactions = new_transaction_list

    def __str__(self):
        return "Queue = {0} priceSet = {1}".format(self.transactions, self.price_set)

    def __repr__(self):
        return "Queue = {0} priceSet = {1}".format(self.transactions, self.price_set)










