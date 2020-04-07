import numpy as np
import pandas as pd

def uniform_prior(grid):
    """Compute a uniform prior over a grid of parameters.
     NOTE: this assumes that
     - last endpoint is the max value of the parameter
     - first endpoint is the min value
    grid: array of params
    
    returns: prior probability over grid that is uniform"""
    return np.repeat((grid[-1] - grid[0]) / len(grid), len(grid))

def grid_approx(prior, likelihood, grid):
    """Use a grid approximation to compute the posterior.
    prior: function (grid of parameters -> prior probability for each grid param)
    likelihood: function (grid of parameters -> likelihood for each grid param)
    grid: array of params
    
    returns: posterior probablity of each grid param"""
    non_normalized = prior(grid) * likelihood(grid)
    normalization_factor = np.sum(non_normalized)
    return non_normalized / normalization_factor

def sample(posterior_vals: pd.Series, num: int):
    """Sample from the posterior distribution in the given df.
    posterior_df: df with the index being parameter values
    posterior_col: column in the df containing posterior distribution values
    num: number of samples to return
    
    returns: sample generator"""
    return np.random.choice(
        a=posterior_vals.index.values,
        size=num,
        p=posterior_vals.values
    )
    