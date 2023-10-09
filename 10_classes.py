class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def print(self):
    print(self)
  def __str__(self):
    return f"{self.name} is {self.age} years"
  def __del__(self):
        print('Destructor called, ' + str(type(self).__name__) + ' is deleted.')

person = Person("John", 36)
person.age=41
person.print()

class Student(Person):
  def __init__(self, fname, lname, graduation):
    super().__init__(fname, lname)
    self.graduationyear = graduation
  def __str__(self):
    return f"{self.name} is {self.age} years and graduated {self.graduationyear}"

student = Student("Maria", 21, 2022)
student.print()