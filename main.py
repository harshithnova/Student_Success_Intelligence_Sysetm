from src.load_data import (
    load_dataset,
    preview_dataset,
    dataset_info
)

df = load_dataset("data/students.csv")

preview_dataset(df)

dataset_info(df)