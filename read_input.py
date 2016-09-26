__author__ = 'ajitkumar'
from companies.Companies import Companies
from companies.Company import Company
from transaction.Transaction import Transaction
from helper.date_helper import convert_to_epoch_time
from helper.order_helper import process_order
from helper.file_helper import read_input_from_file

FILE_NAME = "input.txt"

input_data = read_input_from_file(FILE_NAME)
companies = Companies()
for data in input_data:
    if not companies.is_present(data[2]):
        company = Company(data[2])
        companies.add_new_company(company)
    else:
        company = companies.return_company_object(data[2])
    time = convert_to_epoch_time(data[1])
    transaction = Transaction(data[0], data[3], data[5], time, data[4])
    if transaction.transaction_type.lower() == "buy":
        company.buy_queue.insert(transaction)
        process_order(company)
    else:
        company.sell_queue.insert(transaction)
        process_order(company)










