__author__ = 'ajitkumar'


def process_order(company):
    sell_queue = company.sell_queue
    buy_queue = company.buy_queue
    i = 0
    j = 0
    while i < len(buy_queue.transactions):
        buy = buy_queue.transactions[i]
        while j < len(sell_queue.transactions):
            sell = sell_queue.transactions[j]
            if sell.price <= buy.price:
                if sell.no_of_stocks > buy.no_of_stocks:
                    sell.no_of_stocks = sell.no_of_stocks - buy.no_of_stocks
                    print "{0} {1} {2}".format(sell.order_number,
                                               buy.no_of_stocks, sell.price)
                    i = -1
                    buy_queue.pop()
                else:
                    buy.no_of_stocks = buy.no_of_stocks - sell.no_of_stocks
                    print "{0} {1} {2}".format(sell.order_number,
                                               sell.no_of_stocks, sell.price)
                    j = -1
                    sell_queue.pop()
            else:
                return
            j += 1
        i += 1
    return




