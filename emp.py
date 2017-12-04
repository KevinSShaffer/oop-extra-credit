#!/usr/bin/python

class Employee:

#'Common base class for all employees'

   empCount = 0

   def __init__(self, name, salary, age, taughtClass):

      self.name = name

      self.salary = salary

      self.age = age

      self.taughtClass = taughtClass

      Employee.empCount += 1

   def displayCount(self):

      print("Total Employee ", Employee.empCount)

   def displayEmployee(self):

      print("Name : ", self.name, ", Salary: ", self.salary, ", Age: ", self.age, ", Class: ", self.taughtClass)

"This would create first object of Employee class"

emp1 = Employee("Marlu", 2000, 25, "OOP")

"This would create second object of Employee class"

emp2 = Employee("Ashis", 5000, 25, "OOP")

emp1.displayEmployee()

emp2.displayEmployee()

print("Total Employees: ", Employee.empCount)