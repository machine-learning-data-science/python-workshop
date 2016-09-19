import numpy as np


class Account:

    def __init__(self):
        self.amount = 0

    def put_money(self, deposit):
        print("my amount is", self.amount)
        self.amount += deposit
        print("my amount is", self.amount)

    def take_money(self, withdrawal):
        self.amount -= withdrawal

    def print_amount(self):
        print("my amount is", self.amount)
        print(self.amount)


class BankAccount:

    def __init__(self):
        self.accounts = [Account() for i in np.arange(1000)]

    def put_money(self, account, deposit):
        self.accounts[account].putMoney(deposit)

    def take_money(self, account, withdrawal):
        self.accounts[account].takeMoney(withdrawal)

    def print_amount(self, account):
        self.accounts[account].printAmount()

a = BankAccount()
a.put_money(5, 100)
a.print_amount(5)
