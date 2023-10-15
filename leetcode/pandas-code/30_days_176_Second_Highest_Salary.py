import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_sal = employee['salary'].sort_values(ascending=False).drop_duplicates()
    res = [None if sorted_sal.size < 2 else sorted_sal.iloc[1]]
    return pd.DataFrame({'SecondHighestSalary': res})