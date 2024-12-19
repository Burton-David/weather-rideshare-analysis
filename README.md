# Weather Impact on Ride-sharing Analysis

## Overview
This repository contains a data science analysis of weather impacts on ride-sharing demand. The analysis includes data generation, statistical analysis, and visualization of weather patterns' effects on ride-sharing services.

## Project Structure
```
weather_rideshare_analysis/
├── data/                    # Data files
│   ├── weather_rideshare_data.csv
│   └── summary_statistics.csv
├── scripts/                 # Analysis scripts
│   └── weather_analysis.py
├── images/                  # Generated visualizations
│   ├── demand_timeline.png
│   ├── temp_demand_scatter.png
│   ├── precipitation_impact.png
│   └── correlation_heatmap.png
└── weather_rideshare_analysis.md  # Main analysis article
```

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

## Setup
1. Clone the repository:
```bash
git clone https://github.com/Burton-David/weather-rideshare-analysis.git
cd weather-rideshare-analysis
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn
```

4. Run the analysis:
```bash
cd scripts
python weather_analysis.py
```

## Analysis Results
The complete analysis is available in `weather_rideshare_analysis.md`. Key findings include:
- Temporal patterns in ride-sharing demand
- Temperature effects on service usage
- Precipitation impact analysis
- Weather factor correlations

## License
MIT License

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.