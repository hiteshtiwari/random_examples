import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts.loc[(accounts.income < 20000), 'Low Salary'] = 1
    accounts.loc[(accounts.income >= 20000) & (accounts.income <= 50000), 'Average Salary'] = 1
    accounts.loc[(accounts.income > 50000), 'High Salary'] = 1
    melt_df = pd.melt(accounts, id_vars=['account_id'], value_vars=['Low Salary', 'Average Salary', 'High Salary'],  var_name='category', value_name='accounts_count').fillna(0)

    return melt_df.groupby(['category'])['accounts_count'].sum().reset_index()
