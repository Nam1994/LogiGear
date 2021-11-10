class Checkout(object):
    def __init__(self, email, card_numbers, exp_date, cvc, postal):
        self.email = email
        self.care_numbers = card_numbers
        self.exp_date = exp_date
        self.cvc = cvc
        self.postal = postal

    def __str__(self):
        return "Email is %s, Card Number is %s, Date is %s, CVC is %s, Postal is %s" % (self.email, self.care_numbers,
                                                                                        self.exp_date, self.cvc, self.postal)
