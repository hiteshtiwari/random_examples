import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    uniq_sal = employee['salary'].drop_duplicates()
    sal = uniq_sal.sort_values(ascending=False)
    
    if N > len(sal):
        
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    nth_highest = sal.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})