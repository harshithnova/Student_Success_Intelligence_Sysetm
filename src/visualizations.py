import os

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


CHART_FOLDER = "outputs/charts"

sns.set_style("whitegrid")


def create_output_folder():
    os.makedirs(CHART_FOLDER, exist_ok=True)


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(
        os.path.join(CHART_FOLDER, filename),
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()


# --------------------------------------------------
# Distribution Charts
# --------------------------------------------------

def grade_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["g3"],
        bins=15,
        kde=True
    )

    plt.title("Final Grade Distribution")
    plt.xlabel("Final Grade")
    plt.ylabel("Student Count")

    save_chart("01_grade_distribution.png")


def age_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(df["age"])

    plt.title("Age Distribution")
    plt.xlabel("Age")

    save_chart("02_age_distribution.png")


def absence_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.histplot(df["absences"])

    plt.title("Absence Distribution")
    plt.xlabel("Absences")

    save_chart("03_absence_distribution.png")


# --------------------------------------------------
# Comparison Charts
# --------------------------------------------------

def gender_performance(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="sex",
        y="g3"
    )

    plt.title("Gender vs Final Grade")

    save_chart("04_gender_performance.png")


def studytime_performance(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="studytime",
        y="g3"
    )

    plt.title("Study Time vs Final Grade")

    save_chart("05_studytime_performance.png")


def failures_performance(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="failures",
        y="g3"
    )

    plt.title("Failures vs Final Grade")

    save_chart("06_failures_performance.png")


def performance_category_chart(df):

    plt.figure(figsize=(10, 6))

    sns.countplot(
        data=df,
        x="performance_category"
    )

    plt.title("Performance Category Distribution")

    save_chart("07_performance_categories.png")


# --------------------------------------------------
# Scatterplots
# --------------------------------------------------

def absences_vs_grade(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="absences",
        y="g3"
    )

    plt.title("Absences vs Final Grade")

    save_chart("08_absences_vs_grade.png")


def g1_vs_g3(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="g1",
        y="g3"
    )

    plt.title("G1 vs Final Grade")

    save_chart("09_g1_vs_g3.png")


def g2_vs_g3(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="g2",
        y="g3"
    )

    plt.title("G2 vs Final Grade")

    save_chart("10_g2_vs_g3.png")


def efficiency_vs_grade(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="study_efficiency_score",
        y="g3"
    )

    plt.title("Study Efficiency vs Final Grade")

    save_chart("11_efficiency_vs_grade.png")


# --------------------------------------------------
# Risk Analysis
# --------------------------------------------------

def risk_distribution(df):

    plt.figure(figsize=(10, 6))

    sns.countplot(
        data=df,
        x="risk_level"
    )

    plt.title("Risk Level Distribution")

    save_chart("12_risk_distribution.png")


def persona_distribution(df):

    plt.figure(figsize=(12, 6))

    sns.countplot(
        data=df,
        x="student_persona"
    )

    plt.xticks(rotation=20)

    plt.title("Student Persona Distribution")

    save_chart("13_persona_distribution.png")


# --------------------------------------------------
# Heatmaps
# --------------------------------------------------

def correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=np.number)

    plt.figure(figsize=(14, 10))

    sns.heatmap(
        numeric_df.corr(),
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    save_chart("14_correlation_heatmap.png")


def top_predictors_heatmap(df):

    numeric_df = df.select_dtypes(include=np.number)

    correlations = (
        numeric_df
        .corr()[["g3"]]
        .sort_values(
            by="g3",
            ascending=False
        )
    )

    plt.figure(figsize=(8, 10))

    sns.heatmap(
        correlations,
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation with Final Grade")

    save_chart("15_top_predictors_heatmap.png")


# --------------------------------------------------
# Violin Plots
# --------------------------------------------------

def studytime_violin(df):

    plt.figure(figsize=(10, 6))

    sns.violinplot(
        data=df,
        x="studytime",
        y="g3"
    )

    plt.title("Study Time Distribution by Grade")

    save_chart("16_studytime_violin.png")


def failures_violin(df):

    plt.figure(figsize=(10, 6))

    sns.violinplot(
        data=df,
        x="failures",
        y="g3"
    )

    plt.title("Failures Distribution by Grade")

    save_chart("17_failures_violin.png")


# --------------------------------------------------
# Additional Analyst Charts
# --------------------------------------------------

def parental_education(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="medu",
        y="g3"
    )

    plt.title("Mother Education vs Final Grade")

    save_chart("18_mother_education.png")


def attendance_risk(df):

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="attendance_risk_score",
        y="g3"
    )

    plt.title("Attendance Risk Score vs Final Grade")

    save_chart("19_attendance_risk.png")


def stability_vs_grade(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x="academic_stability_index",
        y="g3"
    )

    plt.title("Academic Stability vs Final Grade")

    save_chart("20_stability_vs_grade.png")


# --------------------------------------------------
# Main Visualization Pipeline
# --------------------------------------------------

def generate_all_visualizations(df):

    print("\nGenerating Visualizations...")
    print("-" * 50)

    create_output_folder()

    grade_distribution(df)
    age_distribution(df)
    absence_distribution(df)

    gender_performance(df)
    studytime_performance(df)
    failures_performance(df)
    performance_category_chart(df)

    absences_vs_grade(df)
    g1_vs_g3(df)
    g2_vs_g3(df)
    efficiency_vs_grade(df)

    risk_distribution(df)
    persona_distribution(df)

    correlation_heatmap(df)
    top_predictors_heatmap(df)

    studytime_violin(df)
    failures_violin(df)

    parental_education(df)
    attendance_risk(df)
    stability_vs_grade(df)

    print("20 visualizations saved successfully")