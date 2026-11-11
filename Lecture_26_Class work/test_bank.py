import pytest
import bank

def test_initial_balance():
    account = bank.BankAccount("Irina", 200.00)
    assert account.balance == 200.00

def test_deposit_success():
    account = bank.BankAccount("Irina", 200.00)
    account.deposit(100.00)
    assert account.balance == 300.00

def test_deposit_negative():
    account = bank.BankAccount("Irina", 200.00)
    with pytest.raises(ValueError):
        account.deposit(-50.00)
    
def test_withdraw_success():
    account = bank.BankAccount("Irina", 300.00)
    account.withdraw(100.00)
    assert account.balance == 200.00

def test_withdraw_insufficient_balance():
    account = bank.BankAccount("Irina", 200.00)
    with pytest.raises(ValueError):
        account.withdraw(300.00)

def test_withdraw_negative():
    account = bank.BankAccount("Irina", 200.00)
    with pytest.raises(ValueError):
        account.withdraw(-50.00)    