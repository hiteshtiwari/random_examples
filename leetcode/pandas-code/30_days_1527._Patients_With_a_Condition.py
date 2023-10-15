import pandas as pd
#approch 1
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients[(patients['conditions'].str.match(r'DIAB1[0-9]*|[A-Z0-9\s]+ DIAB1[0-9]*'))]
    return result

#approch 2
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients[(patients['conditions'].str.contains(r'\bDIAB1'))]
    return result