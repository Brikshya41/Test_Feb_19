'''Create a Employee class and initialize it with first_name, last_name and salary. Also,it has a derived attribute
called email, which is self generated when instance is created. Now, make methods to:
      a. Display - It should display all informations of the employee.'''

class Employee(object):
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def email_done(self):
        self.email = self.first_name.lower() + "." + self.last_name.lower() + "@deerwalk.edu.np"

    def display(self):
        print("{}\n{}\n{}\n{}\n".format(self.first_name, self.last_name, self.salary, self.email))


emp = Employee("Annie", "Frank", "50000")
emp.email_done()
emp.display()
