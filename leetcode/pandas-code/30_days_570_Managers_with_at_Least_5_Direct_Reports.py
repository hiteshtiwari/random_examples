import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    A = employee.groupby(['managerId'])['id'].count().reset_index()
    filter_df = A[A['id'] >= 5][['managerId', 'id']]
    
    joined_df = filter_df.merge(employee, how='right', left_on=filter_df['managerId'], right_on=employee['id']).reset_index()
    
    return joined_df[joined_df['id_x'] >= 5.0][['name']]