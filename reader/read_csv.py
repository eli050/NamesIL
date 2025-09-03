import pandas as pd


class ReadCSV:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> pd.DataFrame:
        """Read CSV file and return as DataFrame."""
        df = pd.read_csv(self.file_path)
        return df