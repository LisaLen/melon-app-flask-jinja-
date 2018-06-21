"""Customers at Hackbright."""


class Customer(object):
        """Ubermelon customer."""

        def __init__(self, first_name, last_name, email, pswd):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.pswd = pswd

        def __repr__(self):
            """ Convenience method to view customer info in console"""

            return "<Customer info: {} {} {}>".format(self.first_name, self.last_name, self.email)

    # TODO: need to implement this

def read_customers_from_file(filepath):
    """Returns dictionary of customer information retrieved from file, email as key"""

    customer_by_email = {}

    for line in open(filepath):
        (first_name,
        last_name,
        email,
        pswd) = line.strip().split("|")
        customer_by_email[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    pswd) 
    return customer_by_email



def  get_by_email(email):

    return customer_by_email[email] 



customer_by_email = read_customers_from_file("customers.txt")