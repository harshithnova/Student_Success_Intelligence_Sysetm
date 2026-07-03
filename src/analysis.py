import pandas as pd
import numpy as np


def dataset_overview(df):
    """
    Basic dataset statistics.
    """

    overview = {
        "total_students": len(df),
        "total_features": df.shape[1],
        "average_grade": round(df["g3"].mean(), 2),
        "median_grade": round(df["g3"].median(), 2),
        "highest_grade": df["g3"].max(),
        "lowest_grade": df["g3"].min()
    }

    return overview


def demographic_analysis(df):
    """
    Analyze performance across demographics.
    """

    results = {
        "gender_performance":
            df.groupby("sex")["g3"]
            .mean()
            .sort_values(ascending=False),

        "address_performance":
            df.groupby("address")["g3"]
            .mean()
            .sort_values(ascending=False),

        "age_performance":
            df.groupby("age")["g3"]
            .mean()
            .sort_values(ascending=False)
    }

    return results


def study_behavior_analysis(df):
    """
    Analyze study habits and performance.
    """

    results = {
        "studytime_performance":
            df.groupby("studytime")["g3"]
            .mean(),

        "schoolsup_performance":
            df.groupby("schoolsup")["g3"]
            .mean(),

        "paid_class_performance":
            df.groupby("paid")["g3"]
            .mean()
    }

    return results


def family_background_analysis(df):
    """
    Analyze family influence.
    """

    results = {
        "mother_education":
            df.groupby("medu")["g3"]
            .mean(),

        "father_education":
            df.groupby("fedu")["g3"]
            .mean(),

        "family_size":
            df.groupby("famsize")["g3"]
            .mean()
    }

    return results


def attendance_analysis(df):
    """
    Analyze attendance impact.
    """

    attendance_corr = round(
        df["absences"].corr(df["g3"]),
        3
    )

    attendance_summary = (
        df.groupby("attendance_risk_score")["g3"]
        .mean()
        .reset_index()
    )

    return {
        "attendance_correlation": attendance_corr,
        "attendance_summary": attendance_summary
    }


def failure_analysis(df):
    """
    Analyze impact of previous failures.
    """

    failure_summary = (
        df.groupby("failures")["g3"]
        .mean()
        .reset_index()
    )

    return failure_summary


def performance_segmentation(df):
    """
    Analyze performance categories.
    """

    segmentation = (
        df["performance_category"]
        .value_counts()
        .reset_index()
    )

    segmentation.columns = [
        "performance_category",
        "student_count"
    ]

    return segmentation


def risk_analysis(df):
    """
    Analyze risk levels.
    """

    risk_summary = (
        df["risk_level"]
        .value_counts()
        .reset_index()
    )

    risk_summary.columns = [
        "risk_level",
        "student_count"
    ]

    return risk_summary


def high_performer_analysis(df):
    """
    Students with G3 >= 16.
    """

    high_performers = df[df["g3"] >= 16]

    summary = {
        "student_count": len(high_performers),
        "average_absences":
            round(high_performers["absences"].mean(), 2),

        "average_studytime":
            round(high_performers["studytime"].mean(), 2),

        "average_failures":
            round(high_performers["failures"].mean(), 2)
    }

    return summary


def low_performer_analysis(df):
    """
    Students with G3 < 10.
    """

    low_performers = df[df["g3"] < 10]

    summary = {
        "student_count": len(low_performers),
        "average_absences":
            round(low_performers["absences"].mean(), 2),

        "average_studytime":
            round(low_performers["studytime"].mean(), 2),

        "average_failures":
            round(low_performers["failures"].mean(), 2)
    }

    return summary


def strongest_predictors(df):
    """
    Rank variables by relationship with G3.
    """

    numeric_columns = df.select_dtypes(
        include=np.number
    )

    correlations = (
        numeric_columns
        .corr()["g3"]
        .sort_values(ascending=False)
        .reset_index()
    )

    correlations.columns = [
        "feature",
        "correlation_with_g3"
    ]

    return correlations


def statistical_summary(df):
    """
    Detailed statistics for G3.
    """

    stats = {
        "mean":
            round(df["g3"].mean(), 2),

        "median":
            round(df["g3"].median(), 2),

        "std":
            round(df["g3"].std(), 2),

        "variance":
            round(df["g3"].var(), 2),

        "25_percentile":
            round(df["g3"].quantile(0.25), 2),

        "75_percentile":
            round(df["g3"].quantile(0.75), 2)
    }

    return stats


def run_full_analysis(df):
    """
    Run every analysis module.
    """

    results = {
        "dataset_overview":
            dataset_overview(df),

        "demographic_analysis":
            demographic_analysis(df),

        "study_behavior_analysis":
            study_behavior_analysis(df),

        "family_background_analysis":
            family_background_analysis(df),

        "attendance_analysis":
            attendance_analysis(df),

        "failure_analysis":
            failure_analysis(df),

        "performance_segmentation":
            performance_segmentation(df),

        "risk_analysis":
            risk_analysis(df),

        "high_performer_analysis":
            high_performer_analysis(df),

        "low_performer_analysis":
            low_performer_analysis(df),

        "strongest_predictors":
            strongest_predictors(df),

        "statistical_summary":
            statistical_summary(df)
    }

    return results