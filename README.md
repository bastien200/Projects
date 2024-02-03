# Titanic Survival Prediction Model

## Description
This project involves the development of a predictive model to determine the likelihood of survival for passengers aboard the Titanic. The code is implemented in Python using popular data science libraries such as pandas, matplotlib, numpy, and scikit-learn. The primary focus is on utilizing the k-nearest neighbors (KNN) classification algorithm to make survival predictions based on features like age, sex, and passenger class.

## Code Overview
1. **Data Loading and Exploration:**
   - The project begins by loading the dataset ('Titanic_Passengers.csv') using the pandas library.
   - Basic information about the dataset, such as the first and last few rows, column names, and data types, is displayed for initial exploration.

2. **Data Cleaning:**
   - The 'Age' column is processed to handle missing values by replacing them with the mean age.
   - The 'Survived' column is cleaned by replacing any instances of '#No#' with 'No'.
   - The 'Sex' column is converted from categorical values ('male', 'female') to numerical values (1, 0).

3. **Data Preparation:**
   - The input features (X) and target variable (Y) are defined based on selected columns ('Age', 'Sex', 'Pclass').
   - The dataset is split into training and testing sets using the train_test_split function from scikit-learn.

4. **Model Training and Evaluation:**
   - A KNN classifier is instantiated with the number of neighbors set to 5.
   - The model is trained using the training dataset.
   - Predictions are made on the test dataset, and the accuracy of the model is calculated and printed.

## Conclusion
This project provides a comprehensive example of building a machine learning model for predicting Titanic passenger survival. It covers data loading, cleaning, and preparation, followed by the training and evaluation of the KNN classifier. The code can serve as a foundational template for more complex machine learning projects and provides insights into the survival factors for Titanic passengers.
