import pandas as pd
# approch 1
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    d = {'name': 'Customers'}
    
    df = customers[~customers['id'].isin(orders['customerId'])]
    result_df = df[['name']].rename(columns=d)
    return result_df

# approach 2
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    d = {'name': 'Customers'}
    comb_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    result_df = comb_df[(comb_df.customerId.isna())][['name']].rename(columns=d)

    return result_df