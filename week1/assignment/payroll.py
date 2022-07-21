# ------------------- ToDo --------------------------
# Create HTML Form to receive Inputs 


# from Employee import Employee
import webbrowser
import os
from dataclasses import dataclass

@dataclass
class Employee:
    first_name: str
    last_name: str
    emp_id: int
    hourly_wage: float
    
    def get_first_name(self):
        return self.first_name
    def set_first_name(self,first_name):
        self.first_name = first_name
        
    def get_last_name(self):
        return self.first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
        
    def get_emp_id(self):
        return self.emp_id
    def set_emp_id(self, emp_id):
        self.emp_id = emp_id
        
    def get_hourly_wage(self):
        return self.hourly_wage
    def set_hourly_wage(self, hourly_wage):
        self.hourly_wage = hourly_wage

    def pay(self, hours):
        if float(hours) <= 40:
            total_pay = float(int(hours) * int(self.hourly_wage))
            print(f" Here is your payout.. ${total_pay}")
            return f" Here is your payout.. ${total_pay}"

        elif float(hours) > 40:
            overtime_pay = float((int(hours) - 40) * (int(self.hourly_wage) * 1.5)) + (40 * int(self.hourly_wage)) 
            print(f"Here is your payout, including overtime... ${overtime_pay:.2f}")
            return f"Here is your payout, including overtime... ${overtime_pay:.2f}"
  

new_employee = Employee(
    input('Please enter Employee ID: '),
    input('Enter Employee First Name: '),
    input('Enter Employee Last Name: '),
    input('Enter Hourly Wage: ')
    
)

current_pay = new_employee.pay(input("Enter hours worked: "))


# to open/create a new html file in the write mode
f = open('week1/assignment/index.html', 'w')
  
# the html code which will go in the file 
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>Hello World</header>
    <h1>{0}</h1>
    <h1>{4}</h1>
    <h1>{2}</h1>
    <h1>{1}</h1>
    <h1>{0}</h1>
    <h1>{3}</h1>
</body>
</html>
""".format(current_pay, "Hello", "to","the","World", )
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()

print("test",os.getcwd())

filename = 'file:///'+os.getcwd()+'/week1/assignment/' + 'index.html'
webbrowser.open_new_tab(filename)

# id_input = input("Please ener the Employee ID: ")
# print(f"Your ID is: {id_input}")

# first_name_input = input("Please enter your first name: ")
# last_name_input = input("Please enter you last name.")
# print(f"Hello {first_name_input} {last_name_input}. Please follow the prompts..")

# hours_input = input("How many hours did you work? ")
# print(f"You worked {hours_input} hours.")

# wage_input = float(input("What is your hourly wage? "))
# print(f"Your hourly wage is: ${wage_input:.2f}.")

# print("--------------------------------")

# def pay():
#     if float(hours_input) <= 40:
#         total_pay = int(hours_input) * int(wage_input)
#         print(f" Here is your payout.. ${total_pay}")

#     elif float(hours_input) > 40:
#         overtime_pay = ((int(hours_input) - 40) * (int(wage_input) * 1.5)) + (40 * int(wage_input)) 
#         print(f"Here is your payout, including overtime... ${overtime_pay:.2f}")
# pay()
# total_pay = int(hours_input) * int(wage_input)
# print(f"You made ${total_pay}.")

    # def __init__(self,first_name, last_name, emp_id, hourly_wage):
    #         self.first_name: first_name
    #         self.last_name: last_name
    #         self.emp_id: emp_id
    #         self.hourly_wage: hourly_wage