import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    first_join = students.merge(subjects, how='cross')
    
    
    res = examinations.groupby(["student_id", "subject_name"]).agg(b_min=pd.NamedAgg(column="subject_name", aggfunc="count")).reset_index()

    join_df = first_join.merge(res, how="left", on=["student_id", "subject_name"])
    return join_df.fillna(0).rename(columns={'b_min':'attended_exams'}).sort_values(['student_id', 'subject_name'])[['student_id', 'student_name', 'subject_name', 'attended_exams']]