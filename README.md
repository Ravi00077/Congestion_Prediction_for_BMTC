# BMTC Bus Congestion Prediction

## Project Overview
This project involves the creation and analysis of a dataset related to the BMTC (Bangalore Metropolitan Transport Corporation) bus transportation system. The goal is to predict congestion levels in various parts of the city based on different factors such as time of day, bus occupancy, weather conditions, and traffic data. The project employs a **Random Forest Classifier** to provide predictions, enabling better planning and decision-making for transportation authorities.

## Dataset Creation
The key attributes of the dataset include:
- **Bus ID**: Identifier for each bus.
- **Time of Day**: Timestamp of when the data was recorded.
- **Route**: The bus route number.
- **Occupancy**: The number of passengers in the bus.
- **Weather Conditions**: Weather data such as temperature, humidity, and rainfall at the time of the journey.
- **Traffic Conditions**: Traffic congestion data from traffic monitoring systems.
- **Congestion Level**: Target variable indicating the level of congestion (Low, Medium, High).

## Data Preprocessing
Before training the model, the following preprocessing steps were applied:
- Handling missing values using imputation techniques.
- Encoding categorical variables (e.g., bus route, congestion levels) using one-hot encoding.
- Normalizing continuous features (e.g., temperature, occupancy) using `StandardScaler`.
- Splitting the dataset into training and test sets for model evaluation.

## Machine Learning Model
To predict bus congestion, a **Random Forest Classifier** was implemented. Random Forest is an ensemble learning method that combines multiple decision trees to provide more robust and accurate predictions. The model was tuned using grid search to find the optimal hyperparameters. The model was evaluated using accuracy and other classification metrics (precision, recall, F1-score).

## Prediction of Congestion
The final model predicts the congestion level for a given bus based on input features such as time of day, route, occupancy, weather, and traffic conditions. This can help the BMTC to optimize scheduling, improve passenger experience, and reduce overcrowding during peak hours.

## Results
The **Random Forest Classifier** was the chosen model, and after hyperparameter tuning, it achieved an accuracy of **97.5%** on the test set. The model demonstrated a good ability to predict congestion in the bus system, with high recall for medium and high congestion levels.

## Future Work
- Incorporate real-time data for more accurate predictions.
- Expand the dataset to include more routes and buses.
- Implement a user-friendly interface to visualize predictions and congestion alerts.

## Installation & Usage

### Prerequisites
- Python 3.x
- `sklearn`, `pandas`, `numpy`, `matplotlib` (or any other required libraries)

### Install Required Libraries
```bash
pip install -r requirements.txt
