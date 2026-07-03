import pandas as pd


def clean_column_names(df):
    """
    Standardize column names.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def remove_duplicates(df):
    """
    Remove duplicate records.
    """

    initial_rows = len(df)

    df = df.drop_duplicates()

    removed = initial_rows - len(df)

    print(f"\nDuplicate Rows Removed: {removed}")

    return df


def handle_missing_values(df):
    """
    Handle missing values.
    """

    missing_count = df.isnull().sum().sum()

    print(f"\nTotal Missing Values: {missing_count}")

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    categorical_columns = df.select_dtypes(include=["object"]).columns

    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(df[column].mode()[0])

    return df


def validate_grades(df):
    """
    Ensure grade columns are within valid range.
    """

    grade_columns = ["g1", "g2", "g3"]

    for column in grade_columns:

        invalid_count = (
            (df[column] < 0) |
            (df[column] > 20)
        ).sum()

        if invalid_count > 0:
            print(
                f"{column}: {invalid_count} invalid values found"
            )

            df = df[
                (df[column] >= 0) &
                (df[column] <= 20)
            ]

    return df


def generate_data_quality_report(df):
    """
    Create a quick data quality summary.
    """

    report = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.values,
        "missing_values": df.isnull().sum().values,
        "unique_values": df.nunique().values
    })

    return report


def clean_data(df):
    """
    Main cleaning pipeline.
    """

    print("\nStarting Data Cleaning...")
    print("-" * 50)

    df = clean_column_names(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = validate_grades(df)

    print("\nData Cleaning Complete")

    return df