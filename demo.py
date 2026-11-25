"""Demonstration of the DataPulse package."""
import pandas as pd
from datapulse import DataPulseToolkit

sample = pd.DataFrame({
    "Student Name": ["Ana", "Ben", "Cara", "Ben", "Dino"],
    "Study Hours": [2, 4, 3, 4, None],
    "Quiz Score": [70, 85, 78, 85, 90],
})

toolkit = DataPulseToolkit(fill_value=0)

print("Original data:")
print(sample)
print("\\nCleaned data:")
cleaned = toolkit.prepare(sample, missing="mean")
print(cleaned)
print("\\nStatistics:")
print(toolkit.analyzer.describe(cleaned))
print("\\nCorrelation:")
print(toolkit.analyzer.correlation(cleaned))
print("\\nColumn summary:")
print(toolkit.analyzer.column_summary(cleaned, "quiz_score"))

toolkit.visualizer.histogram(cleaned, "quiz_score", output="outputs/quiz_scores.png")
print("\\nChart saved to outputs/quiz_scores.png")
print("Toolkit modules:", len(toolkit))
