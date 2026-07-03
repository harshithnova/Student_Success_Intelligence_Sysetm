import pandas as pd


def generate_grade_insights(df):

    insights = []

    average_grade = df["g3"].mean()

    insights.append(
        f"The average final grade across all students is "
        f"{average_grade:.2f}."
    )

    excellent_students = (
        (df["performance_category"] == "Excellent")
        .sum()
    )

    insights.append(
        f"{excellent_students} students achieved "
        f"excellent academic performance."
    )

    return insights


def generate_failure_insights(df):

    insights = []

    no_failures = (
        df[df["failures"] == 0]["g3"]
        .mean()
    )

    previous_failures = (
        df[df["failures"] > 0]["g3"]
        .mean()
    )

    insights.append(
        "Students with prior academic failures "
        "consistently score lower than students "
        "with no failure history."
    )

    insights.append(
        f"Average grade without failures: "
        f"{no_failures:.2f}"
    )

    insights.append(
        f"Average grade with failures: "
        f"{previous_failures:.2f}"
    )

    return insights


def generate_attendance_insights(df):

    insights = []

    attendance_correlation = (
        df["absences"]
        .corr(df["g3"])
    )

    insights.append(
        f"Attendance has a correlation of "
        f"{attendance_correlation:.2f} "
        f"with final grades."
    )

    if attendance_correlation < 0:
        insights.append(
            "Higher absenteeism is associated "
            "with lower academic performance."
        )

    return insights


def generate_risk_insights(df):

    insights = []

    risk_counts = (
        df["risk_level"]
        .value_counts()
    )

    high_risk_students = (
        risk_counts.get("High Risk", 0)
    )

    medium_risk_students = (
        risk_counts.get("Medium Risk", 0)
    )

    insights.append(
        f"{high_risk_students} students are "
        f"classified as High Risk."
    )

    insights.append(
        f"{medium_risk_students} students are "
        f"classified as Medium Risk."
    )

    insights.append(
        "These students should be prioritized "
        "for academic intervention."
    )

    return insights


def generate_study_insights(df):

    insights = []

    study_performance = (
        df.groupby("studytime")["g3"]
        .mean()
    )

    best_group = (
        study_performance.idxmax()
    )

    best_grade = (
        study_performance.max()
    )

    insights.append(
        f"Students in study time category "
        f"{best_group} achieved the highest "
        f"average grade of {best_grade:.2f}."
    )

    return insights


def generate_persona_insights(df):

    insights = []

    persona_counts = (
        df["student_persona"]
        .value_counts()
    )

    dominant_persona = (
        persona_counts.idxmax()
    )

    insights.append(
        f"The largest student segment is "
        f"'{dominant_persona}'."
    )

    return insights


def generate_predictor_insights(
        predictor_table
):
    insights = []

    top_predictors = (
        predictor_table
        .head(6)
    )

    for _, row in top_predictors.iterrows():

        feature = row["feature"]

        correlation = (
            row["correlation_with_g3"]
        )

        insights.append(
            f"{feature} shows a correlation "
            f"of {correlation:.3f} with "
            f"final grade."
        )

    return insights


def generate_recommendations(df):

    recommendations = []

    recommendations.append(
        "Implement early-warning monitoring "
        "for students with repeated absences."
    )

    recommendations.append(
        "Provide academic support for "
        "students with previous failures."
    )

    recommendations.append(
        "Track high-risk students weekly."
    )

    recommendations.append(
        "Encourage consistent study habits."
    )

    recommendations.append(
        "Review attendance patterns before "
        "major examinations."
    )

    return recommendations


def generate_all_insights(
        df,
        analysis_results
):

    insights = {
        "grade_insights":
            generate_grade_insights(df),

        "failure_insights":
            generate_failure_insights(df),

        "attendance_insights":
            generate_attendance_insights(df),

        "risk_insights":
            generate_risk_insights(df),

        "study_insights":
            generate_study_insights(df),

        "persona_insights":
            generate_persona_insights(df),

        "predictor_insights":
            generate_predictor_insights(
                analysis_results[
                    "strongest_predictors"
                ]
            ),

        "recommendations":
            generate_recommendations(df)
    }

    return insights