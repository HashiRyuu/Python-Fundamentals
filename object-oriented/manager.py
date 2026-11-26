##
#  Defines an employee of a business.
# 
class Employee :
   ##
   #  Constructs an employee object that contains their name and salary.
   #
   def __init__(self) :
      self._name = ""
      self._baseSalary = 0.0
      
   ##
   #  Sets the name of the employee.
   #  @param newName string containing the employee's name
   #
   def setName(self, newName) :
      self._name = newName
      
   ##
   #  Sets the employee's base salary.
   #  @param newSalary the employee's base salary as a floating-point
   #
   def setBaseSalary(self, newSalary) :
      self._baseSalary = newSalary
      
   ##
   #  Gets the employee's name.
   #  @return a string containing the name
   #
   def getName(self) :
      return self._name
      
   ##
   #  Gets the employee's salary.
   #  @return the salary as a numerical value
   #
   def getSalary(self) :
      return self._baseSalary



#  Defines a manager, who is an employee, but with more responsibility.
# Part 1
class Manager(Employee):
   def __init__(self):
      super().__init__()
      self._bonus = 0
   
   def setBonus(self, amount):
      self._bonus += amount
   
   def getBonus(self):
      return self._bonus


#  Defines a manager, who is an employee, but with more responsibility.
# Part 2
class Manager(Employee) :
   ##
   #  Constructs a manager object with a default bonus of $0.
   #
   def __init__(self) :
      super().__init__()
      self._bonus = 0.0
    
   ##
   #  Sets the manager's bonus.
   #  @param amount the amount of the bonus as a numerical value
   #
   def setBonus(self, amount) :
      self._bonus = amount
    
   ##
   #  Gets the value of the manager's bonus.
   #  @return the bonus as a numerical value
   #
   def getBonus(self) :
      return self._bonus
   
   def getName(self):
      return "*" + super().getName()
   
   def getSalary(self):
      return super().getSalary() + self._bonus
