## Diamond Price Prediction

### Introduction About the Data :

**The dataset** The goal is to predict `price` of given diamond (Regression Analysis).

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

Dataset Source Link :
[https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv) 


# Diamond Price Prediction Project

Welcome to the Diamond Price Prediction project! This project aims to predict the price of diamonds using various regression models. The best model was chosen from among **Linear Regression**, **Lasso**, **Ridge**, **ElasticNet**, and **Decision Tree Regressor**.

## Models Used

### Linear Regression
Linear Regression is a statistical method that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.

### Lasso (Least Absolute Shrinkage and Selection Operator)
Lasso is a type of linear regression that uses shrinkage. Shrinkage is where data values are shrunk towards a central point, like the mean. Lasso adds a penalty equal to the absolute value of the magnitude of coefficients to the linear regression optimization.

### Ridge Regression
Ridge Regression is another linear regression technique that adds a penalty on the size of the coefficients. The penalty term is equal to the square of the magnitude of coefficients. This helps to mitigate multicollinearity and overfitting issues.

### ElasticNet
ElasticNet is a regularized regression method that linearly combines the L1 and L2 penalties of the Lasso and Ridge methods. This allows ElasticNet to inherit the features of both Lasso and Ridge.

### Decision Tree Regressor
Decision Tree Regressor is a non-linear model that splits the data into subsets based on the value of input features. It builds a tree where each node represents a feature, each branch represents a decision rule, and each leaf represents an outcome.

## Project Structure

- **src/**: Contains the source code for the project.
  - **exception/**: Custom exception handling.
  - **logger/**: Logging configuration.
  - **pipelines/**: Prediction pipeline.
  - **utils/**: Utility functions.
- **notebooks/**: Jupyter notebooks for data exploration and model evaluation.
- **data/**: Dataset used for training and testing.
- **artifacts/**: Contains trained models and other artifacts.
- **README.md**: Project documentation.

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/diamond-price-prediction.git

