
import sys
sys.path.append('/vagrant/data-science-from-scratch/code/')  

from statistics import standard_deviation
from multiple_regression import bootstrap_statistic, p_value
import sklearn
from sklearn.linear_model import LinearRegression


def transform_dataframe(X):
    """Given a dataframe X return a list of rows where each row is a
    list of column values"""
    return X.values.tolist()

def prepare_data(X, y):
    return zip(transform_dataframe(X), y)

def run_linear_regression(data):
    """Given data, which is an (X,y) tuple, run linear regression and return 
    the vector of coefficients"""
    X, y = zip(*data)
    lm = LinearRegression()
    lm.fit(X, y)
    return [lm.intercept_] + list(lm.coef_)

def standard_deviations(data):
    """Returns standard deviation of each column of data where data is a list
    of rows and each row is a list of column values"""
    num_columns = len(data[0])
    return [standard_deviation([row[i] for row in data]) 
    for i in range(num_columns)]

def calculate_pvalues(X, y, num_samples):
    """Runs linear regression using predictor variables X to predict target y.
    Estimates p values for coefficients using bootstrap sampling"""
    names = ['Intercept'] + list(X.columns)
    data = prepare_data(X, y)
    betas = run_linear_regression(data)

    bootstrap_betas = bootstrap_statistic(data, run_linear_regression, num_samples)
    sderrs = standard_deviations(bootstrap_betas)

    return { name: p_value(beta, sdev) for 
    name, beta, sdev in zip(names, betas, sderrs)}
