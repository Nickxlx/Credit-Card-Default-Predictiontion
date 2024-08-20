# Credit Card Default Prediction

## Description

Credit Card Default Prediction is a project aimed at predicting whether a credit card holder is likely to default on their payment based on various features. This predictive modeling task helps financial institutions assess and manage credit risk effectively.

## Data

The dataset used in this project can be found on Kaggle: [Default of Credit Card Clients Dataset](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset). Please download it and place it in the project directory as `credit_card_clients.csv`.

## About dataset

There are 25 variables:

- LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
- SEX: Gender (1=male, 2=female)
- EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
- MARRIAGE: Marital status (1=married, 2=single, 3=others)
- AGE: Age in years
- PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, ... 8=payment delay for eight months, 9=payment delay for nine months and above)
- PAY_2: Repayment status in August, 2005 (scale same as above)
- PAY_3: Repayment status in July, 2005 (scale same as above)
- PAY_4: Repayment status in June, 2005 (scale same as above)
- PAY_5: Repayment status in May, 2005 (scale same as above)
- PAY_6: Repayment status in April, 2005 (scale same as above)
- BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
- BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
- BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
- BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
- BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
- BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
- PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
- PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
- PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
- PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
- PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
- PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)

- default.payment.next.month: Default payment (1=yes, 0=no)

## Models

The predictive model employed in this project is an XGBoost classifier. XGBoost is chosen for its high performance in classification tasks and its ability to handle complex datasets effectively.

## Installation

To run this project locally, you can clone the repository using the following command:

```bash
git clone [ Git link](https://github.com/Nickxlx/Credit-Card-Default-Predictiontion/tree/main)

```

## Create a new Conda environment

```
conda create --prefix nenv python==3.8 -y
```

```
conda activate ./nenv
```

Once you have successfully completed the steps above,

## Final Project Run

- Install the **requirements.txt** by running the following command

To install the dependencies

```
pip install -r requirements.txt
```

Run Application

```
python application.py
```

## For prediction go to

http://127.0.0.1:8080

The project should run now in your local pc.

# Data to test the model

70000,1,3,2,42,1,2,2,2,2,0,37042,36171,38355,39423,38659,39362,0,3100,2000,0,1500,1500 = 1 faulty

1e+05,2,3,3,43,0,0,0,0,0,0,61559,51163,43824,39619,35762,33258,2000,1606,1500,2000,1500,1000 = 0 Not faulty

## Contributing

Contributions to improve the project are welcome. Feel free to fork the repository, create pull requests, or open issues for any suggestions or bug reports.

## Contact

For questions or feedback regarding the project, you can reach out to the project owner at [nikhilsinghxlx@gmail.com](mailto:nikhilsinghxlx@gmail.com).
