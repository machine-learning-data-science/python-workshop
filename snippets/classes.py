from __future__ import print_function
import numpy as np


class Account:

    def __init__(self):
        self.amount = 0

    def putMoney(self, deposit):
        print("my amount is", self.amount)
        self.amount += deposit
        print("my amount is", self.amount)

    def takeMoney(self, withdrawal):
        self.amount -= withdrawal

    def printAmount(self):
        print("my amount is", self.amount)
        print(self.amount)


class BankAccount:

    def __init__(self):
        self.accounts = [Account() for i in np.arange(1000)]

    def putMoney(self, account, deposit):
        self.accounts[account].putMoney(deposit)

    def takeMoney(self, account, withdrawal):
        self.accounts[account].takeMoney(withdrawal)

    def printAmount(self, account):
        self.accounts[account].printAmount()

a = BankAccount()
a.putMoney(5, 100)
a.printAmount(5)
