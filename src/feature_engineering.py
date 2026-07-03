import numpy as np
import pandas as pd


def create_performance_category(final_grade):
    """
    Categorize students based on final grade.
    """

    if final_grade >= 16:
        return "Excellent"

    elif final_grade >= 13:
        return "Good"

    elif final_grade >= 10:
        return "Average"

    return "At Risk"


def calculate_attendance_risk(absences):
    """
    Higher absences indicate higher risk.
    """

    if absences >= 20:
        return 5

    elif absences >= 15:
        return 4

    elif absences >= 10:
        return 3

    elif absences >= 5:
        return 2

    return 1


def calculate_academic_risk(row):
    """
    Composite academic risk score.
    Higher score = higher risk.
    """

    risk_score = 0

    risk_score += row["failures"] * 4

    risk_score += row["attendance_risk_score"] * 2

    risk_score += (20 - row["g1"]) * 0.5

    risk_score += (20 - row["g2"]) * 0.5

    return round(risk_score, 2)


def assign_risk_level(score):
    """
    Convert risk score into categories.
    """

    if score >= 20:
        return "High Risk"

    elif score >= 12:
        return "Medium Risk"

    return "Low Risk"


def create_study_efficiency_score(row):
    """
    Performance achieved per study unit.
    """

    study_time = row["studytime"]

    if study_time == 0:
        return 0

    return round(row["g3"] / study_time, 2)


def create_academic_stability_index(row):
    """
    Lower value means more consistent performance.
    """

    grades = [row["g1"], row["g2"], row["g3"]]

    return round(np.std(grades), 2)


def create_student_persona(row):
    """
    Create simple student personas.
    """

    if row["g3"] >= 16 and row["failures"] == 0:
        return "High Achiever"

    if row["studytime"] >= 3 and row["g3"] < 10:
        return "Hardworking Struggler"

    if row["absences"] >= 15:
        return "Attendance Risk"

    if row["academic_risk_score"] >= 20:
        return "Academic Risk"

    return "Typical Student"


def engineer_features(df):
    """
    Main feature engineering pipeline.
    """

    print("\nCreating engineered features...")
    print("-" * 50)

    engineered_df = df.copy()

    # Performance category
    engineered_df["performance_category"] = (
        engineered_df["g3"]
        .apply(create_performance_category)
    )

    # Attendance risk
    engineered_df["attendance_risk_score"] = (
        engineered_df["absences"]
        .apply(calculate_attendance_risk)
    )

    # Growth between assessments
    engineered_df["performance_growth"] = (
        engineered_df["g2"]
        - engineered_df["g1"]
    )

    # Improvement before final exam
    engineered_df["final_improvement_score"] = (
        engineered_df["g3"]
        - engineered_df["g2"]
    )

    # Study efficiency
    engineered_df["study_efficiency_score"] = (
        engineered_df
        .apply(create_study_efficiency_score, axis=1)
    )

    # Stability
    engineered_df["academic_stability_index"] = (
        engineered_df
        .apply(create_academic_stability_index, axis=1)
    )

    # Academic risk
    engineered_df["academic_risk_score"] = (
        engineered_df
        .apply(calculate_academic_risk, axis=1)
    )

    # Risk category
    engineered_df["risk_level"] = (
        engineered_df["academic_risk_score"]
        .apply(assign_risk_level)
    )

    # Student persona
    engineered_df["student_persona"] = (
        engineered_df
        .apply(create_student_persona, axis=1)
    )

    print("Feature engineering completed")

    return engineered_df