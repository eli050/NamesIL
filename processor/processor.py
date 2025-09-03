import pandas as pd


class DataProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def sum_of_value(self, column_name: str, value:int|str, sum_column: str) -> int:
        return self.df[self.df[column_name] == value][sum_column].sum()

    def sum_of_grouped_values(self, group_by_columns: list[str],
                              column_name: str, value: int|str, sum_column: str) -> pd.DataFrame:
        grouped_df = self.df.groupby(group_by_columns, group_keys= True).apply(
            lambda x: (x[sum_column] * (x[column_name] == value)).sum(),include_groups=True
        ).reset_index(name="n")

        return grouped_df

