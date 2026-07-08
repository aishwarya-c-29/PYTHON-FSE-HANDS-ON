from abc import ABC, abstractmethod


# S - Single Responsibility Principle
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class EmployeeReport:
    def generate_report(self, employee):
        print("Employee:", employee.name)
        print("Salary:", employee.get_salary())


# O - Open/Closed Principle
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):
    def pay(self):
        print("Paid using UPI")


# L - Liskov Substitution Principle
class Vehicle:

    def start(self):
        print("Vehicle started")


class Car(Vehicle):

    def start(self):
        print("Car started")


# I - Interface Segregation Principle
class Printer:

    def print_document(self):
        print("Printing document")


class Scanner:

    def scan_document(self):
        print("Scanning document")


# D - Dependency Inversion Principle
class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):

    def connect(self):
        print("Connected to MySQL Database")


class Application:

    def __init__(self, database):
        self.database = database

    def run(self):
        self.database.connect()


# Main Program

# SRP
emp = Employee("Aishwarya", 50000)
report = EmployeeReport()
report.generate_report(emp)

# OCP
payment = CreditCard()
payment.pay()

payment = UPI()
payment.pay()

# LSP
vehicle = Car()
vehicle.start()

# ISP
printer = Printer()
printer.print_document()

scanner = Scanner()
scanner.scan_document()

# DIP
db = MySQL()
app = Application(db)
app.run()

"""
Output:
Employee: Varun
Salary: 50000
Paid using Credit Card
Paid using UPI
Car started
Printing document
Scanning document
Connected to MySQL Database
"""
