import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    num_order_df = orders.groupby('customer_number')['order_number'].count().reset_index()
    result = num_order_df.sort_values(['order_number'], ascending=False)[['customer_number']].head(1)

    return result