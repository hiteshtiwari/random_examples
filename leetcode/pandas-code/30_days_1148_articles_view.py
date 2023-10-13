import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result_df = views[(views['author_id'] == views['viewer_id'])].drop_duplicates(['author_id'])[['author_id']].rename(columns={'author_id': 'id'})
    return result_df.sort_values(['id'])
    