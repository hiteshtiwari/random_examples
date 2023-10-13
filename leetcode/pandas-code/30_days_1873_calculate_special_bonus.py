import pandas as pd

#Approach 1
import numpy as np


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    
    employees['bonus'] =  np.where((employees['employee_id'] % 2 != 0) & (employees['name'].astype(str).str[0] != 'M'),employees['salary'],0 )
    
    return employees[['employee_id', 'bonus']].sort_values(['employee_id'])
    
    
#Approach 2
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    
    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].astype(str).str[0] != 'M'), 'bonus' ] = employees['salary']
    
    return employees[['employee_id', 'bonus']].sort_values(['employee_id'])
