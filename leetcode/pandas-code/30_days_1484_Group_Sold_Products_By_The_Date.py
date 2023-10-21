import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    sort_df = activities.drop_duplicates().groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()

    sort_df.columns = ['sell_date', 'num_sold', 'products']
    
    result = sort_df.sort_values(by='sell_date')

    return result 
    