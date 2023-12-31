import pandas as pd

# approach 1
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    res1 = products[~products['store1'].isnull()][['product_id', 'store1']].rename(columns={'store1': 'price'})
    res2 = products[~products['store2'].isnull()][['product_id', 'store2']].rename(columns={'store2': 'price'})
    res3 = products[~products['store3'].isnull()][['product_id', 'store3']].rename(columns={'store3': 'price'})
    res1['store'] = 'store1'
    res2['store'] = 'store2'
    res3['store'] = 'store3'
    frames = [res1, res2, res3]
    return pd.concat(frames)

# approach 2
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    
    return pd.melt(products, id_vars='product_id', value_vars=['store1', 'store2', 'store3'], var_name="store", value_name="price").dropna()    