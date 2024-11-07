# Daily Usage Analysis

This repository contains a comprehensive analysis of daily usage patterns in a service-based dataset. Through this project, we aim to explore key factors influencing user engagement and identify trends over different time periods.

## Dataset Overview

The dataset used in this project includes various environmental and time-based variables collected daily. Key features include:
- **Date (`dteday`)**: The specific date of data entry.
- **Season and Weather (`season_hour`, `weathersit_hour`)**: Information on the season and weather conditions.
- **Temperature and Humidity (`temp_day`, `hum_day`)**: Reflects daily temperature and humidity levels.
- **User Counts**: Split into casual users (`casual_day`), registered users (`registered_day`), and total count (`cnt_day`).

### Key Analysis Goals
The analysis is designed to address several questions:
1. **Impact of Seasons and Weather on Usage**: How do weather conditions and seasonal changes affect user behavior?
2. **Usage Trends Over Time**: Identify any growth or decline trends in usage over time.
3. **Differences Between Casual and Registered Users**: Highlight distinct patterns between casual and registered user groups.
4. **Correlation Between Temperature and User Engagement**: Explore the impact of temperature variations on daily usage.

## Methodology

The analysis is divided into several steps:
1. **Data Cleaning**: Ensuring data consistency and handling missing values.
2. **Exploratory Data Analysis (EDA)**: Identifying patterns and correlations.
3. **Feature Engineering**: Creating additional variables that may improve model predictions.
4. **Visualization**: Generating graphs to showcase insights.

## Visual Insights

Some of the visualizations included:
- **Seasonal Usage Patterns**: A bar chart showing average user counts by season.
- **Temperature vs. Usage Scatter Plot**: Illustrating the correlation between temperature and total usage.
- **Casual vs. Registered Usage Comparison**: A line graph comparing casual and registered user trends over time.

## Repository Structure
- `notebooks/`: Jupyter Notebooks for in-depth analysis and visualization.
- `data/`: Contains the main dataset used for this analysis.
- `README.md`: Overview of the project, analysis goals, and key insights.

## Future Work
Further analysis can explore:
- **Weather Prediction**: Using machine learning models to predict user counts based on weather data.
- **User Segmentation**: Clustering users based on behavioral patterns.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir analisis-pinjaman-sepeda
cd analisis-pinjaman-sepeda
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```
