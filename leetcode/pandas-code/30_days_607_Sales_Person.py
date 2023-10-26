import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    s_c_df = sales_person.merge(orders, how="left", on="sales_id")[['name', 'com_id']]
    s_c_o_df = s_c_df.merge(company, how="left", on="com_id")
    name_with_RED = s_c_o_df[(s_c_o_df['name_y'] == 'RED')][['name_x']]
    
    res = sales_person.merge(name_with_RED, how='left', left_on='name', right_on='name_x')
    
    return res[res['name_x'].isna()][['name']]
    