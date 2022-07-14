
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