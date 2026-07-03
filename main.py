from src.load_data import (
    load_dataset,
    preview_dataset,
    dataset_info
)

from src.cleaning import (
    clean_data,
    generate_data_quality_report
)

from src.feature_engineering import (
    engineer_features
)


df = load_dataset("data/students.csv")

preview_dataset(df)

dataset_info(df)

df = clean_data(df)

quality_report = generate_data_quality_report(df)

df = engineer_features(df)

print("\nEngineered Features")
print("-" * 50)

print(
    df[
        [
            "g3",
            "performance_category",
            "academic_risk_score",
            "risk_level",
            "student_persona"
        ]
    ].head()
)