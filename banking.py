from abc import ABC, abstractmethod

# ----------------------
# CLASS: Account (abstract class)
# PURPOSE: Blueprint for all account types
# ----------------------


class Account(ABC):

    # Abstract methods — must be implemented by child classes
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

# ----------------------
# CLASS: SavingsAccount
# INHERITS: Account (blueprint)
# ----------------------


class SavingsAccount(Account):

    # Constructor (__init__) — define attributes
    def __init__(self, owner, balance=0):
        self.owner = owner               # Public attribute
        self.__balance = balance         # Private attribute (Encapsulation)

    # ----------------------
    # METHOD: deposit
    # BEHAVIOR: add money to balance
    # ----------------------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    # ----------------------
    # METHOD: withdraw
    # BEHAVIOR: remove money from balance
    # ----------------------
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    # ----------------------
    # METHOD: get_balance
    # BEHAVIOR: return current balance
    # ----------------------
    def get_balance(self):
        return self.__balance


# ----------------------
# OBJECT: acc1
# TYPE: SavingsAccount
# ----------------------
acc1 = SavingsAccount("Kwame", 1000)

# Test methods
acc1.deposit(500)
acc1.withdraw(200)
print(f"Balance: {acc1.get_balance()}")
