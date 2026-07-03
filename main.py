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

from src.analysis import (
    run_full_analysis
)

from src.visualizations import (
    generate_all_visualizations
)
from src.insights import (
    generate_all_insights
)


def main():

    print("\n" + "=" * 60)
    print("STUDENT SUCCESS INTELLIGENCE SYSTEM")
    print("=" * 60)

    # Load dataset
    df = load_dataset("data/students.csv")

    # Preview dataset
    preview_dataset(df)

    # Dataset information
    dataset_info(df)

    # Clean data
    df = clean_data(df)

    # Data quality report
    quality_report = generate_data_quality_report(df)

    print("\nData Quality Report")
    print("-" * 60)
    print(quality_report.head())

    # Feature engineering
    df = engineer_features(df)

    print("\nEngineered Features Preview")
    print("-" * 60)

    engineered_columns = [
        "g3",
        "performance_category",
        "attendance_risk_score",
        "academic_risk_score",
        "risk_level",
        "student_persona"
    ]

    print(df[engineered_columns].head())

    # Analysis
    analysis_results = run_full_analysis(df)

    # Visualizations
    generate_all_visualizations(df)

    print("\nVisualizations Generated Successfully")
    print("-" * 60)
    
    # Generate insights
    insights = generate_all_insights(
        df,
        analysis_results
    )

    print("\nDataset Overview")
    print("-" * 60)
    print(analysis_results["dataset_overview"])

    print("\nStatistical Summary")
    print("-" * 60)
    print(analysis_results["statistical_summary"])

    print("\nTop 10 Success Predictors")
    print("-" * 60)
    print(
        analysis_results["strongest_predictors"]
        .head(10)
    )

    print("\nPerformance Segmentation")
    print("-" * 60)
    print(
        analysis_results["performance_segmentation"]
    )

    print("\nRisk Analysis")
    print("-" * 60)
    print(
        analysis_results["risk_analysis"]
    )

    print("\nHigh Performer Profile")
    print("-" * 60)
    print(
        analysis_results["high_performer_analysis"]
    )

    print("\nLow Performer Profile")
    print("-" * 60)
    print(
        analysis_results["low_performer_analysis"]
    )

    print("\nAnalysis Completed Successfully")
    print("=" * 60)
    
    print("\nKey Insights")
    print("-" * 60)

    for category, values in insights.items():

        print(f"\n{category.upper()}")

        for item in values:
            print(f"• {item}")


if __name__ == "__main__":
    main()