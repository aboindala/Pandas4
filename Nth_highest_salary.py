import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df =employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N>len(df) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        df2 = df.iloc[N-1]
        return pd.DataFrame({f'getNthHighestSalary({N})':[df2]})