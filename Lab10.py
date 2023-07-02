# Program Name: Lab10.py
# Course: IT1114/Section W02
# Student Name: Farzam Dizna
# Assignment Number: Lab10
# Due Date: 04/16/2023
# Purpose: This class will store the Employee Number, Office Number, Name (First and Last), Birthdate, Total Number of hours worked, and Total number of overtime hours worked.
# Source1: https://www.w3schools.com/python/python_classes.asp
# Source2: https://www.programiz.com/python-programming/datetime
# Source3: https://stackoverflow.com/questions/55879461/enter-date-of-birth
# Source4: https://stackabuse.com/how-to-format-dates-in-python/
# Source5: https://www.programiz.com/python-programming/exceptions
# Source6: https://www.w3schools.com/python/python_try_except.asp
# Source 7: https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
# Source 8: https://www.w3schools.com/python/gloss_python_raise.asp
# Source 9: https://www.freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python/

class Worker:
    def __init__(self):                                 # constructor that initializes the members of the class
        self.employee_number = None
        self.office_number = None
        self.name = None
        self.birthdate = None
        self.hours_worked = 0
        self.hours_overtime = 0
        self.hourly_salary = 0
        self.overtime_salary = 0
        
    def get_employee_number(self):                      # returns the employee number
        return self.employee_number
    def set_employee_number(self, x):                   # changes the employee number
        if not isinstance(x, int):                      # if the employee number is not an integer we raise an error that states that the employee number has to be an integer 
            raise ValueError("The employee number must be an integer")
        self.employee_number = x
    
    def get_office_number(self):                        # returns the office number
        return self.office_number
    def set_office_number(self, x):                     # if office number is less than 100 or greater than 500 we return false, otherwise we return true
        if x < 100 or x > 500:                          # if the office number is less than 100 or greater than 500 then we raise an error that states that the value should be between 100 and 500
            raise ValueError("The office number must be between 100 and 500")
        self.office_number = x
       
    def get_name(self):                                 # returns the first and last name
        return self.name
    def set_name(self, x):                              # sets the first and last name
        if not x:
            raise ValueError("The name can not be empty")    # if the name is empty then we throw an exception saying that it cannot be empty
        x = x.replace(" ", "")                          # removes empty space in the name
        x = x.replace("_", "")                          # removes "_" from the name
        x = x.replace(".", "")                          # removes "." from the name
        x = x.replace("-", "")                          # removes "-" from the name
        self.name = x
    
    def get_birthdate(self):                            # returns the birthday
        return self.birthdate
    def set_birthdate(self, d, m, y):                   # sets the birthday format
        if m < 1 or m > 12:                             # if the month is less than 1 or greater than 12 we throw an exception stating that it must be bewteen 1 and 12
            raise ValueError("The month must be between 1 and 12")
        if d < 1 or d > 31:                             # if the day is less than 1 or greater than 31 we throw an exception stating that it should be between 1 and 31
            raise ValueError("The day must be between 1 and 31")
        self.birthdate = (d, m, y)
     
    def get_hours_worked(self):                         # returns the number of hours worked
        return self.hours_worked
    def add_hours(self, x):                             # if the number of hours being added is greater then 9 we add 9 hours to the total hours worked, and then we add the remainder to the total overtime
        if x < 0:                                       # if the number of hours being added is less than 0 then we throw an exception and state that it can not be less than 0
            raise ValueError("The number of hours can not be less than 0")
        if x > 9:
            self.hours_worked += 9
            self.hours_overtime += (x - 9)
        else:
            self.hours_worked += x
    def get_hours_overtime(self):                       # returns the number of overtime hours worked
        return self.hours_overtime
    
    def set_hourly_salary(self, x):                     # sets the worker's hourly salary if the salary given is greater than 0
        if x < 0:
            return False
        else:
            self.hourly_salary = x
            return True
    
    def set_overtime_salary(self, x):                   # sets the worker's overtime salary if the value is greater than 0
        if x < 0:
            return False
        else:
            self.overtime_salary = x
            return True
    
    def get_hourly_salary(self):                        # returns the hourly salary
        return self.hourly_salary
    def get_overtime_salary(self):                      # returns the overtime salary
        return self.overtime_salary
    def get_pay(self):                                  # returns the worker's total pay by calculating the pay
        return (self.hours_worked * self.hourly_salary) + (self.hours_overtime * self.overtime_salary)

