#EMPLOYEE SALARY AND DETAILS
class Employee:
    
    def __init__(self):
        self.emp_id=input("enter the emp_id:")
        self.emp_name=input("enter the emp_name:")
        self.emp_salary=int(input("enter the emp_salary:"))
        self.emp_dept=input("enter the emp_dept:")
        
    def calculate_emp_salary(self,emp_salary,hours_worked):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amount=(overtime*(self.emp_salary/50))
            self.emp_salary+=overtime_amount
            return self.emp_salary
            
        else:
            return self.emp_salary
        
    def emp_assign_dept(self):
           self.emp_dept="cse"
           return self.emp_dept
        
    def print_employee_details(self):
        return self.emp_id,self.emp_name,self.emp_salary,self.emp_dept
        
        
        
e1=Employee()
print("employee details are:",e1.print_employee_details())
print("the total salary is:",e1.calculate_emp_salary(500,500))
print("the assigned dept",e1.emp_dept,"is converted to:",e1.emp_assign_dept())
e2=Employee()
e3=Employee()
e4=Employee()
