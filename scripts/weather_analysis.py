import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set the style for all visualizations
plt.style.use('bmh')  # Using a built-in style that works well for data visualization
sns.set_theme(style="whitegrid")  # Set seaborn style properly

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
n_days = len(dates)

# Create weather data
weather_data = pd.DataFrame({
    'date': dates,
    'temperature': np.random.normal(20, 10, n_days),  # Mean temp of 20°C with variation
    'precipitation': np.random.exponential(2, n_days),  # Exponential distribution for precipitation
    'wind_speed': np.random.normal(15, 5, n_days),  # Wind speed in km/h
})

# Create ride demand data with weather influence
base_demand = 1000
weather_influence = (
    -0.3 * weather_data['precipitation'] +  # Negative impact of rain
    0.2 * np.sin((weather_data['temperature'] - 20) * np.pi / 30) +  # Optimal temp around 20°C
    -0.1 * (weather_data['wind_speed'] - 15) / 5  # Slight negative impact of wind
)

# Add seasonal and weekly patterns
day_of_week = pd.Series(dates.dayofweek)
weekend_effect = (day_of_week >= 5).astype(float) * 0.3
seasonal_effect = 0.2 * np.sin(2 * np.pi * np.arange(n_days) / 365)

# Calculate final demand
demand = base_demand * (1 + weather_influence + weekend_effect + seasonal_effect)
demand = demand * np.random.normal(1, 0.1, n_days)  # Add random noise
weather_data['ride_demand'] = demand.astype(int)

# Ensure the images directory exists
import os
os.makedirs('../images', exist_ok=True)
os.makedirs('../data', exist_ok=True)

# Save the dataset
weather_data.to_csv('../data/weather_rideshare_data.csv', index=False)

# Create visualizations
plt.figure(figsize=(12, 6))
plt.plot(weather_data['date'], weather_data['ride_demand'], linewidth=2)
plt.title('Ride-sharing Demand Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Rides', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../images/demand_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

# Temperature vs Demand scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=weather_data, x='temperature', y='ride_demand', alpha=0.5)
plt.title('Temperature vs Ride Demand', fontsize=14)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Number of Rides', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../images/temp_demand_scatter.png', dpi=300, bbox_inches='tight')
plt.close()

# Precipitation impact
plt.figure(figsize=(10, 6))
sns.boxplot(data=weather_data,
            x=pd.qcut(weather_data['precipitation'], q=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']),
            y='ride_demand')
plt.title('Impact of Precipitation on Ride Demand', fontsize=14)
plt.xlabel('Precipitation Level', fontsize=12)
plt.ylabel('Number of Rides', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../images/precipitation_impact.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate correlation matrix
correlation_matrix = weather_data[['temperature', 'precipitation', 'wind_speed', 'ride_demand']].corr()

# Create correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Matrix of Weather Factors and Ride Demand', fontsize=14)
plt.tight_layout()
plt.savefig('../images/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate summary statistics
summary_stats = weather_data.describe()
summary_stats.to_csv('../data/summary_statistics.csv')

print("Analysis complete! All visualizations and data have been saved successfully.")