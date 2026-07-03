from src.load_data import (
    load_dataset,
    preview_dataset,
    dataset_info
)

from src.cleaning import (
    clean_data,
    generate_data_quality_report
)


df = load_dataset("data/students.csv")

preview_dataset(df)

dataset_info(df)

df = clean_data(df)

quality_report = generate_data_quality_report(df)

print("\nData Quality Report")
print("-" * 50)
print(quality_report.head())