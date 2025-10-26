# Persian Books Text Classification using Naive Bayes

A machine learning project that implements a Naive Bayes classifier for categorizing Persian books into 6 distinct categories.

## Overview

This project demonstrates text classification on Persian language texts using the Naive Bayes algorithm. The classifier processes book titles and descriptions to automatically categorize them into predefined categories.

## Categories

1. Management and Business (مدیریت و کسب و کار)
2. Novels (رمان)
3. Islamic Studies (کلیات اسلام)
4. Children and Young Adult Stories (داستان کودک و نوجوانان)
5. Sociology (جامعه‌شناسی)
6. Short Stories (داستان کوتاه)

## Features

- **Persian Language Processing**: Uses Hazm library for Persian text processing
- **Text Preprocessing**: Includes stop word removal and stemming
- **Naive Bayes Classification**: Implements probabilistic text classification
- **Bag-of-Words Model**: Converts text to numerical features
- **Smoothing**: Uses Laplace smoothing (epsilon = 0.5) to handle zero probabilities

## Dependencies

- NumPy
- Pandas
- Hazm (Persian NLP library)

## Usage

```bash
python final_code.py
```

## How It Works

1. **Data Preprocessing**: Removes special characters and stop words from book titles and descriptions
2. **Tokenization**: Splits text into individual words using Persian tokenizer
3. **Stemming**: Reduces words to their root forms
4. **Training**: Builds a bag-of-words model for each category
5. **Classification**: Calculates probabilities using Naive Bayes algorithm
6. **Evaluation**: Reports accuracy on test dataset

## Dataset

- Training data: `books_train.csv`
- Test data: `books_test.csv`
- Stop words: `sw.csv`

## Algorithm

The classifier uses the Naive Bayes approach with:

- Prior probability based on category distribution
- Likelihood calculated from word frequencies in each category
- Logarithmic probabilities to handle numerical underflow
- Laplace smoothing to prevent zero probability issues

