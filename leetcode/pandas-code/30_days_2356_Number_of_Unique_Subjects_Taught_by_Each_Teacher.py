import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher[['teacher_id', 'subject_id']].drop_duplicates().groupby('teacher_id')['subject_id'].count().reset_index()
    return result.rename(columns = {'subject_id':'cnt'})