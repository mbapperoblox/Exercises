"""OOP problems: inheritance.

A subclass is written class Child(Parent).
super() gives access to the parent class, and a method with the same
name in the child overrides the parent's method.
"""


# ------------------------------------------------------------ Problem 1
class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


# ------------------------------------------------------------ Problem 2
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return (f"Hi, I am {self.name}, I am {self.age} years old "
                f"and I live at {self.address}.")


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)   # reuse the parent constructor
        self.field_of_study = field_of_study

    def introduce(self):
        return (f"Hi, I am {self.name}, a student of "
                f"{self.field_of_study}. I live at {self.address}.")


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return (f"Hi, I am {self.name} and I work at {self.company}. "
                f"I live at {self.address}.")


# ------------------------------------------------------------ Problem 3
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        """Returns True if done, False if the balance is not enough."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, destination, amount):
        """Moves money to another account. False if balance is insufficient."""
        if not self.withdraw(amount):
            return False
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate      # 0.02 means 2%

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def check_balance(self):
        return self.balance


# ------------------------------------------------------------ tests
if __name__ == "__main__":
    # Problem 1 (polymorphism: same call, different result)
    for v in [Vehicle(), Car(), Bicycle()]:
        print("P1:", v.drive())

    # Problem 2
    people = [
        Person("Sam", 40, "5 rue Verte"),
        Student("Aya", 21, "12 rue des Lilas", "Data Science"),
        Employee("Tom", 35, "3 av. Foch", "Airbus"),
    ]
    for p in people:
        print("P2:", p.introduce())

    # Problem 3
    acc1 = BankAccount("FR001", 100)
    sav = SavingsAccount("FR002", 200, interest_rate=0.05)

    print("P3: transfer 50 ->", acc1.transfer(sav, 50),
          "| acc1 =", acc1.balance, "| sav =", sav.check_balance())
    print("P3: transfer 500 ->", acc1.transfer(sav, 500),
          "| acc1 =", acc1.balance)
    sav.add_interest()
    print("P3: after interest, sav =", sav.check_balance())   # 250 * 1.05 = 262.5
