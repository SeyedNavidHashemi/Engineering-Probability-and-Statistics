# Engineering Statistics Solutions

This repository contains solutions to three mini assignments covering probability distributions, statistical analysis, and Bayesian inference.

## Overview

The project demonstrates practical implementation of statistical concepts including Poisson distributions, coupon collector problems, and Bayesian probability updates using Python.

## Questions

### Question 1: Poisson Distribution Analysis
- Analyzes metro and BRT transit data to identify Poisson distributions
- Estimates distribution parameters using maximum likelihood estimation
- Compares empirical distributions with theoretical Poisson distributions
- Demonstrates the additive property of Poisson random variables

### Question 2: Coupon Collector Problem
- Implements a simulation-based approach to solve the coupon collector problem
- Derives moment generating functions (MGFs) for geometric distributions
- Computes expected values using MGF properties
- Validates theoretical results through empirical simulation

### Question 3: Bayesian Inference
- Applies Bayesian probability updates to digit classification
- Implements Beta-Bernoulli conjugate prior-posterior analysis
- Visualizes probability distributions dynamically as new data arrives
- Demonstrates practical application of Bayes' theorem

## Technologies Used

- **Python 3**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **SciPy** - Statistical functions and probability distributions
- **SymPy** - Symbolic mathematics
- **Jupyter Notebook** - Interactive development

## Key Statistical Concepts

- **Poisson Distribution**: Parameter estimation and distribution fitting
- **Geometric Distribution**: Moment generating functions
- **Binomial Distribution**: Probability mass functions
- **Bayesian Inference**: Prior-posterior updates with conjugate priors
- **Monte Carlo Simulation**: Empirical validation of theoretical results

## Usage

Each question is contained in a separate Jupyter notebook:
- `Q1.ipynb` - Poisson distribution analysis
- `Q2.ipynb` - Coupon collector problem
- `Q3.ipynb` - Bayesian inference for digit classification

Run the notebooks using Jupyter:
```bash
jupyter notebook
```

## Data Files

The project requires the following data files (not included in repository):
- `Tarbiat.csv` - Metro and BRT usage data
- `digits.csv` - Handwritten digit dataset
- `EPS_Fall_1402.pdf` - Course assignment description
