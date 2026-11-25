# DataPulse – Data Science Toolkit

**DataPulse** is a beginner-friendly Python package that helps users perform three common data science tasks: basic data cleaning, descriptive statistics, and simple visualization.

## Features
- Standardizes column names and removes duplicate rows.
- Handles missing values using drop, mean, median, or a constant.
- Calculates descriptive statistics and correlation.
- Creates histograms, bar charts, and scatter plots.
- Combines the modules in one reusable `DataPulseToolkit` class.

## Installation
Python 3.9 or newer is recommended.

```bash
pip install -r requirements.txt
pip install -e .
```

## Quick start
```python
import pandas as pd
from datapulse import DataPulseToolkit

data = pd.DataFrame({
    "Study Hours": [2, 4, 3, 5],
    "Quiz Score": [70, 85, 78, 92]
})

tool = DataPulseToolkit()
clean_data = tool.prepare(data)
print(tool.analyzer.describe(clean_data))
print(tool.analyzer.correlation(clean_data))
tool.visualizer.scatter_plot(clean_data, "study_hours", "quiz_score",
                             output="outputs/study_vs_score.png")
```

## Run the demonstration
```bash
python demo.py
```

## Run tests
```bash
python -m unittest discover -s tests
```

## Package structure
```text
datapulse_oop_project/
├── datapulse/
│   ├── __init__.py
│   ├── base.py
│   ├── cleaning.py
│   ├── statistics.py
│   ├── visualization.py
│   └── toolkit.py
├── tests/
│   └── test_datapulse.py
├── demo.py
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
```

## OOP concepts used
- **Classes:** `DataModule`, `DataCleaner`, `StatisticsAnalyzer`, `DataVisualizer`, and `DataPulseToolkit`.
- **Encapsulation:** private-style attributes such as `_name` and `_fill_value`, accessed through properties.
- **Inheritance:** the three feature modules inherit from `DataModule`.
- **Polymorphism:** each child class overrides the `process()` method with behavior suited to its task.
- **Dunder methods:** `__repr__`, `__str__`, and `__len__` provide readable object information and toolkit length.
- **Composition:** `DataPulseToolkit` contains cleaner, analyzer, and visualizer objects.

## Main methods
`clean()`, `handle_missing()`, `remove_duplicates()`, `rename_columns()`, `describe()`, `column_summary()`, `correlation()`, `top_values()`, `histogram()`, `bar_chart()`, `scatter_plot()`, `prepare()`, and `report()`.

## Contributors
Add your actual group members and their contributions here before submission.

## Notes
This is an educational project. Review the code, run the demo and tests, and update the contributor details before publishing.
