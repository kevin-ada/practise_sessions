class Employee:
    pay_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}{self.last}@company.com"

    @property
    def get_full_name(self):
        return f'{self.first}{self.last}'

    @property
    def get_email(self):
        return f"{self.email}"

    def raise_amount(self):
        self.pay = int(self.pay_amount * self.pay_amount)
