# Week 3 - Advanced Data Analysis and Visualization in Logistics

## Project Overview

This project focuses on advanced data analysis and visualization of a hypothetical logistics dataset using Python. The analysis includes data simulation, exploratory data analysis, visualization of logistics performance metrics, analytical insights, and recommendations for improving logistics operations.

## Objective

The objective of this project is to understand logistics performance using data-driven analysis. Key factors such as delivery time, shipment volume, distance, transportation cost, transport mode, region, and delays are analyzed.

## Dataset

A hypothetical dataset containing 500 shipment records was generated using Python.

The dataset includes:

- Shipment ID
- Region
- Transport Mode
- Priority
- Distance
- Shipment Volume
- Weight
- Delivery Time
- Transport Cost
- Delay Status
- Delay Days

## Exploratory Data Analysis

The analysis includes:

- Descriptive statistics
- Mean and median calculations
- Distribution analysis
- Transport mode comparison
- Regional delay analysis
- Correlation analysis
- Cost and delivery-time analysis

## Visualizations

The project contains six visualizations:

1. Distribution of Delivery Time
2. Transport Cost by Mode
3. Distance vs Transport Cost
4. Transport Mode Performance
5. Correlation Matrix
6. Delay Rate by Region

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

## Key Insights

- Air transportation provides faster delivery but has significantly higher transportation costs.
- Rail transportation provides a lower-cost option for suitable shipments.
- Distance is an important factor affecting both delivery time and transportation cost.
- Delay rates vary across transport modes and regions.
- Visualization helps identify operational bottlenecks and cost drivers.

## Recommendations

- Select transportation modes based on both cost and delivery requirements.
- Use air transportation primarily for urgent shipments.
- Evaluate rail transportation for suitable long-distance shipments.
- Investigate regions with higher delay rates.
- Use distance and shipment characteristics for transportation cost forecasting.
- Monitor delivery-time distributions and delays rather than relying only on averages.

## Reproducibility

The Python script uses a fixed random seed (`42`) so that the simulated dataset can be reproduced consistently.

## Project Files

- `Week3_Advanced_Logistics_Analysis_Report.docx` - Detailed project report
- `week3_logistics_analysis.py` - Python analysis and visualization script
- `logistics_simulated_dataset.csv` - Simulated logistics dataset
- `figures/` - Visualization outputs
