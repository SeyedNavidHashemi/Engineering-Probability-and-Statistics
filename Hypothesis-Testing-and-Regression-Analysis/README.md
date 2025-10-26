# Hypothesis Testing & Regression Analysis

A comprehensive statistical analysis project covering autoencoder reconstruction evaluation, linear regression implementation from scratch, and hypothesis testing using Kolmogorov-Smirnov and Shapiro-Wilk tests.

## Overview

This project implements statistical analysis methods including autoencoder reconstruction evaluation, manual least squares regression, and goodness-of-fit testing using Kolmogorov-Smirnov and Shapiro-Wilk tests. The analysis covers both machine learning model evaluation and traditional statistical techniques using real-world datasets.

## Key Features

### 1. Autoencoder Reconstruction Analysis
- Evaluates reconstruction quality of MNIST digit autoencoder using Mean Squared Error (MSE)
- Performs goodness-of-fit testing using Kolmogorov-Smirnov test
- Analyzes distribution of reconstruction errors across 10,000 test images

### 2. Linear Regression Implementation
- Implements least squares regression from scratch
- Calculates coefficient of determination (R²)
- Analyzes impact of outliers and high-leverage points on regression models
- Demonstrates robustness of linear regression under different data scenarios

### 3. Statistical Data Analysis with FIFA Dataset
- Handles missing data imputation using mean values
- Performs exploratory data analysis with box plots and summary statistics
- Implements random sampling and statistical inference
- Compares empirical distributions with theoretical normal distributions using Q-Q plots
- Performs Shapiro-Wilk normality tests
- Analyzes Poisson distribution convergence at different sample sizes

## Technologies

- **Python** - Core programming language
- **NumPy** - Numerical computations
- **TensorFlow/Keras** - Deep learning framework
- **Pandas** - Data manipulation
- **Matplotlib** - Data visualization
- **SciPy** - Statistical testing functions (Kolmogorov-Smirnov, Shapiro-Wilk)
- **Jupyter Notebooks** - Interactive development and documentation

## Methodology

The project follows rigorous statistical practices:

- **Data Preprocessing**: Missing value imputation using appropriate statistical measures
- **Model Evaluation**: Quantitative assessment using MSE for reconstruction tasks
- **Hypothesis Testing**: Kolmogorov-Smirnov and Shapiro-Wilk tests for distribution analysis
- **Regression Analysis**: Manual implementation of least squares method with mathematical formulation
- **Visualization**: Q-Q plots for distribution comparison, histograms, and scatter plots
- **Reproducibility**: Fixed random seeds for consistent results

## Results

Key findings include:

1. Distribution analysis of autoencoder reconstruction errors
2. Impact assessment of outliers on regression model performance
3. Empirical distribution fitting to theoretical models
4. Sample size effects on statistical testing results

## Structure

```
├── CA3_q1.ipynb          # Autoencoder evaluation and goodness-of-fit testing
├── CA3_q2.ipynb          # Linear regression implementation
├── CA3_q3.ipynb          # FIFA dataset statistical analysis
├── FIFA2020.csv          # Dataset containing FIFA player statistics
```

## Requirements

```
numpy
pandas
matplotlib
scipy
tensorflow
keras
jupyter
```

## Usage

Each Jupyter notebook can be run independently:

1. **CA3_q1.ipynb**: Requires `mnist_AE.h5` pre-trained model file
2. **CA3_q2.ipynb**: Standalone regression analysis
3. **CA3_q3.ipynb**: Requires `FIFA2020.csv` dataset file

Open the notebooks in Jupyter and run all cells to reproduce the analyses.

## Statistical Concepts Demonstrated

- Autoencoder reconstruction quality evaluation using MSE
- Goodness-of-fit testing using Kolmogorov-Smirnov test
- Manual implementation of least squares regression method
- Coefficient of determination (R²) calculation for model assessment
- Q-Q plots for empirical vs theoretical distribution comparison
- Shapiro-Wilk normality test for statistical validation
- Poisson distribution convergence analysis
- Statistical hypothesis testing and p-value interpretation
- Missing data imputation using mean substitution

## Applications

This project showcases practical applications of statistical methods in:
- Machine learning model evaluation
- Regression analysis and model diagnostics
- Empirical data distribution analysis
- Hypothesis testing and statistical inference

