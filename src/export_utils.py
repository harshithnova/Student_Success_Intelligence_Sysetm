# Create the data_exports folder if it doesn't exist.
# This prevents errors when saving files like risk_students.csv.
import os


EXPORT_FOLDER = "outputs/data_exports"


def create_export_folder():
    os.makedirs(
        EXPORT_FOLDER,
        exist_ok=True
    )