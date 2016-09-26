__author__ = 'ajitkumar'


class Companies:
    """
    Class for companies.
    """
    def __init__(self):
        self.companies = set()

    def is_present(self, company_name):
        for company in self.companies:
            if company_name == company.name:
                return True
        return False

    def add_new_company(self, company):
        self.companies.add(company)

    def return_company_object(self, company_name):
        for company in self.companies:
            if company.name == company_name:
                return company
        return None

    def __str__(self):
        return "companies = {0}".format(self.companies)

    def __repr__(self):
        return "companies = {0}".format(self.companies)





