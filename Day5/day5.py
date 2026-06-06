#python inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.student_id = student_id

    def display(self):
        super().display()  # Call the parent class display method
        print(f"Student ID: {self.student_id}")

student = Student("Sangharsha", 22, "S12345")
student.display()

# Example: Polymorphism
class Animal:
    def speak(self):
        raise NotImplementedError()

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal: Animal):
    # Polymorphic call: works with any Animal subclass
    print(animal.speak())

animal_sound(Dog())
animal_sound(Cat())

# Example: Encapsulation
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

acct = BankAccount("Sangharsha", 100)
acct.deposit(50)
acct.withdraw(30)
print(f"Owner: {acct.owner}, Balance: {acct.get_balance()}")
