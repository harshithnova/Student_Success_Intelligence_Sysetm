import pandas as pd


def load_dataset(file_path):
    """
    Load the student dataset and perform
    a few basic validation checks.
    """

    df = pd.read_csv(file_path)

    print("\nDataset Loaded")
    print("-" * 40)
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df


def preview_dataset(df, rows=5):
    """
    Display sample records.
    """

    print("\nDataset Preview")
    print("-" * 40)
    print(df.head(rows))


def dataset_info(df):
    """
    Print dataframe information.
    """

    print("\nDataset Information")
    print("-" * 40)

    print(f"Shape: {df.shape}")
    print("\nMissing Values:")
    print(df.isnull().sum())