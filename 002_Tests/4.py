"""
Rozwiń zadanie 2, w taki sposób by nie można było wypłacić więcej
niż jest w kasie. W takim przypadku program powinien wyżucić wyjątek

"""


from dataclasses import dataclass
from _pytest.python_api import raises
import pytest


@dataclass
class Bank:
    amount: int = 0 

    def add_money(self, money):
        self.amount += money

    def withdraw_money(self, money):
        if money > self.amount:
            raise NotEnoughCash("Nie mam tyle w kasie")
        self.amount -= money
        
        return money

# Rozszerzenie klasy exception
class NotEnoughCash(Exception):
    pass

class TestBank:
    def test_withdraw_over_amount(self):
        #sprawdza czy pojawi się wyjątek w przypadku pojawienia się
        #błędu
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw_money(200)

    

         
