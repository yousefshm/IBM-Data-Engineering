# Airfoil Noise Prediction using Spark ML Pipelines

This project is the final capstone for the **Machine Learning with Apache Spark** course, part of the **IBM Data Engineering Professional Certificate**.

It demonstrates the construction of an end-to-end Machine Learning pipeline using **PySpark**, covering the entire lifecycle from data extraction and cleaning (ETL) to model training, evaluation, and persistence.

## 📂 Project Structure
* **`Final_Project.ipynb`**: The main Jupyter Notebook containing the full code, execution logs, and output metrics.
* **`NASA_airfoil_noise_cleaned.parquet`**: The processed and optimized dataset used for training.

## 🚀 Project Scenario
As a Data Engineer at an aeronautics consulting firm, the objective was to build a scalable pipeline to predict the **Sound Level (Decibels)** of airfoils based on aerodynamic features (Frequency, Angle of Attack, Chord Length, etc.). The solution needed to handle raw data cleaning and automate the transformation steps for production deployment.

## 🛠 Tools & Technologies
* **Compute Engine:** Apache Spark 3.x
* **API:** PySpark (Python)
* **Libraries:** Spark MLlib (Machine Learning), Spark SQL.
* **Formats:** Parquet (Columnar Storage), CSV.

## 📋 Implementation Steps

### 1. ETL & Data Engineering
* **Ingestion:** Loaded raw data from `NASA_airfoil_noise_raw.csv`.
* **Cleaning:**
    * Removed duplicate rows (Row count reduced from 1522 to 1503).
    * Dropped rows with null values (Final count: 1499).
* **Transformation:** Renamed target column to `SoundLevelDecibels` and stored the result in **Parquet** format for optimized reading.

### 2. Machine Learning Pipeline
Constructed a unified Spark Pipeline with the following stages:
1.  **VectorAssembler:** Combines input features into a single vector.
2.  **StandardScaler:** Normalizes features (Standard Deviation = 1, Mean = 0) to ensure model stability.
3.  **LinearRegression:** The algorithm used for predicting the continuous sound level variable.

### 3. Model Evaluation
The model was trained on a 70% split and tested on 30%. The performance metrics achieved are:
* **Mean Squared Error (MSE):** ~22.59
* **Mean Absolute Error (MAE):** ~3.73
* **R-Squared ($R^2$):** ~0.54 (Explains 54% of the variance).

### 4. Model Persistence
To simulate a production environment, the trained pipeline model was:
* Saved to disk under the directory `Final_Project`.
* Reloaded to verify integrity.
* Used to generate predictions on the test dataset effectively.

## 🧠 Key Insights
* **Feature Importance:** The model analysis (coefficients) revealed that **Frequency** (-3.97) and **Chord Length** (-3.38) have the strongest negative correlation with noise levels.
* **Scalability:** By using Spark ML Pipelines, this workflow can easily scale to process terabytes of data without code modification.

---
*To view the code and execution details, please open the `Final_Project.ipynb` file in this repository.*
