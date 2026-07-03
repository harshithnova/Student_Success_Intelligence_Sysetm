# Student Success Intelligence System

A Python pipeline that takes a raw student performance dataset and turns it into something actually useful — cleaned data, engineered risk scores, 20 charts, and a plain-text executive report you can hand to someone who's never opened a CSV in their life.

I built this to go beyond a typical "load data, plot a histogram" school project. The goal was to simulate what an actual student success/early-warning system might look like: flag at-risk students early, explain *why* they're at risk, and summarize it all in a report a teacher or administrator could skim in two minutes.

## What it does

Given a dataset of 649 students (grades, study time, attendance, family background, etc.), the pipeline:

1. **Cleans the data** — standardizes column names, drops duplicates, runs a data quality check
2. **Engineers features**, including:
   - `performance_category` — Excellent / Good / Average / At Risk, based on final grade
   - `attendance_risk_score` — risk score derived from absence count
   - `academic_risk_score` — a composite score combining failures, attendance, and early exam grades
   - `risk_level` — Low / Medium / High Risk, derived from the academic risk score
   - `student_persona` — buckets students into simple archetypes (High Achiever, Hardworking Struggler, Attendance Risk, Academic Risk, Typical Student)
   - `study_efficiency_score`, `academic_stability_index`, and grade growth/improvement metrics
3. **Runs statistical analysis** — dataset overview, demographic breakdowns, correlation analysis, and top predictors of final grade
4. **Generates 20 charts** covering distributions, performance comparisons, correlations, and risk breakdowns
5. **Exports a list of high-risk students** to CSV, so they're easy to pull into a spreadsheet or forward to an advisor
6. **Writes a full executive report** summarizing everything above in plain text

## Why This Project Matters

Student performance problems are often identified too late, after poor results have already occurred.

This project demonstrates how educational data can be transformed into an early-warning system that helps identify struggling students before final examinations and supports data-driven intervention strategies.

## Project structure

```
Student_Success_Intelligence_System/
├── data/
│   └── students.csv           # raw dataset
├── src/
│   ├── load_data.py           # loading + dataset preview
│   ├── cleaning.py            # cleaning + data quality checks
│   ├── feature_engineering.py # risk scores, personas, derived features
│   ├── analysis.py            # statistical analysis + predictors
│   ├── visualizations.py      # chart generation
│   ├── insights.py            # auto-generated written insights
│   ├── report_generator.py    # executive report writer
│   └── export_utils.py        # output folder handling
├── notebooks/
│   └── exploratory_analysis.ipynb
├── outputs/
│   ├── charts/                # 20 generated PNG charts
│   ├── data_exports/          # risk_students.csv
│   └── reports/                # student_success_report.txt
├── main.py                    # runs the full pipeline end to end
└── requirements.txt
```

## Getting started

```bash
git clone https://github.com/harshithnova/Student_Success_Intelligence_System.git
cd Student_Success_Intelligence_System
pip install -r requirements.txt
python main.py
```

That's it — running `main.py` executes the whole pipeline: load → clean → engineer features → analyze → visualize → generate report. Everything gets written to `outputs/`.

## Sample output

Running the pipeline against the included dataset (649 students) produces, among other things:

- **Average final grade:** 11.91 / 20
- Earlier assessment scores (G1 and G2) emerged among the strongest predictors of final grade performance.
- A full risk breakdown across Low / Medium / High Risk students
- A CSV of every student flagged High Risk, ready for follow-up

Check `outputs/reports/student_success_report.txt` after a run for the full executive summary, and `outputs/charts/` for all 20 visualizations.

## Dataset

The dataset (`data/students.csv`) is based on the well-known UCI Student Performance dataset, with fields covering demographics, family background, study habits, and three sets of grades (G1, G2, G3).

## Tech stack

- Python
- pandas / numpy for data wrangling
- matplotlib / seaborn for visualizations
- Jupyter for exploratory work

## Notes

This is a portfolio/learning project — the risk-scoring logic (thresholds, weights, persona rules) is intentionally simple and rule-based rather than ML-driven, so it's easy to read, tweak, and reason about. A natural next step would be swapping the rule-based risk score for a trained classification model.

## Author

Harshith Kanamarlapudi
https://github.com/harshithnova