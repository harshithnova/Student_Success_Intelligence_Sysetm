import os
from datetime import datetime


REPORT_FOLDER = "outputs/reports"


def create_report_folder():
    os.makedirs(
        REPORT_FOLDER,
        exist_ok=True
    )


def write_section(
        file,
        title,
        content
):
    file.write("\n")
    file.write("=" * 70 + "\n")
    file.write(title.upper() + "\n")
    file.write("=" * 70 + "\n\n")
    file.write(content)
    file.write("\n")


def generate_report(
        df,
        analysis_results,
        insights
):

    create_report_folder()

    report_path = (
        f"{REPORT_FOLDER}/"
        f"student_success_report.txt"
    )

    with open(
            report_path,
            "w",
            encoding="utf-8"
    ) as report:

        report.write(
            "STUDENT SUCCESS INTELLIGENCE SYSTEM\n"
        )

        report.write(
            f"Generated: "
            f"{datetime.now()}\n"
        )

        report.write(
            "=" * 70 + "\n"
        )

        # Executive Summary

        overview = (
            analysis_results[
                "dataset_overview"
            ]
        )

        executive_summary = f"""
Total Students Analyzed:
{overview['total_students']}

Average Final Grade:
{overview['average_grade']}

Highest Grade:
{overview['highest_grade']}

Lowest Grade:
{overview['lowest_grade']}
"""

        write_section(
            report,
            "Executive Summary",
            executive_summary
        )

        # Dataset Overview

        dataset_overview = f"""
Rows:
{df.shape[0]}

Columns:
{df.shape[1]}

Engineered Features Added:
Performance Category,
Attendance Risk Score,
Academic Risk Score,
Risk Level,
Study Efficiency Score,
Academic Stability Index,
Student Persona
"""

        write_section(
            report,
            "Dataset Overview",
            dataset_overview
        )

        # Statistical Summary

        stats = (
            analysis_results[
                "statistical_summary"
            ]
        )

        statistical_section = "\n".join(
            [
                f"{key}: {value}"
                for key, value
                in stats.items()
            ]
        )

        write_section(
            report,
            "Statistical Summary",
            statistical_section
        )

        # Top Predictors

        predictors = (
            analysis_results[
                "strongest_predictors"
            ]
            .head(10)
        )

        predictor_text = ""

        for _, row in predictors.iterrows():

            predictor_text += (
                f"{row['feature']} : "
                f"{row['correlation_with_g3']:.3f}\n"
            )

        write_section(
            report,
            "Top Success Factors",
            predictor_text
        )

        # Risk Analysis

        risk_table = (
            analysis_results[
                "risk_analysis"
            ]
        )

        risk_text = ""

        for _, row in risk_table.iterrows():

            risk_text += (
                f"{row['risk_level']} : "
                f"{row['student_count']} students\n"
            )

        write_section(
            report,
            "Risk Analysis",
            risk_text
        )

        # High Performers

        high_perf = (
            analysis_results[
                "high_performer_analysis"
            ]
        )

        high_perf_text = "\n".join(
            [
                f"{k}: {v}"
                for k, v
                in high_perf.items()
            ]
        )

        write_section(
            report,
            "High Performer Profile",
            high_perf_text
        )

        # Low Performers

        low_perf = (
            analysis_results[
                "low_performer_analysis"
            ]
        )

        low_perf_text = "\n".join(
            [
                f"{k}: {v}"
                for k, v
                in low_perf.items()
            ]
        )

        write_section(
            report,
            "Low Performer Profile",
            low_perf_text
        )

        # Insights

        insight_text = ""

        for category, values in insights.items():

            insight_text += (
                f"\n{category.upper()}\n"
            )

            for item in values:

                insight_text += (
                    f"- {item}\n"
                )

        write_section(
            report,
            "Key Findings",
            insight_text
        )

        # Recommendations

        recommendation_text = ""

        for recommendation in (
            insights["recommendations"]
        ):
            recommendation_text += (
                f"- {recommendation}\n"
            )

        write_section(
            report,
            "Recommendations",
            recommendation_text
        )

        # Conclusion

        conclusion = """
Student performance is influenced by
multiple academic and behavioral factors.

Attendance, prior failures and previous
assessment performance emerged as the
strongest indicators of final academic
outcomes.

The risk identification system can be
used to proactively identify students
who may benefit from additional support
and intervention.
"""

        write_section(
            report,
            "Conclusion",
            conclusion
        )

    print(
        f"\nReport saved to: {report_path}"
    )

    return report_path