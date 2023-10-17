import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(department, left_on='departmentId', right_on='id')
    merged_df_new = merged_df.rename(columns = {'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})[['Department', 'Employee', 'Salary']]
    
    return merged_df_new[merged_df_new['Salary'] == merged_df_new.groupby('Department')['Salary'].transform(max)]