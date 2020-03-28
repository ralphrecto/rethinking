import numpy as np

def uniform_prior(grid):
    """Compute a uniform prior over a grid of parameters.
     NOTE: this assumes that
     - last endpoint is the max value of the parameter
     - first endpoint is the min value
    grid: array of params
    
    returns: prior probability over grid that is uniform"""
    return np.repeat(len(grid) / (grid[-1] - grid[0]), len(grid))

def grid_approx(prior, likelihood, grid):
    """Use a grid approximation to compute the posterior.
    prior: function (grid of parameters -> prior probability for each grid param)
    likelihood: function (grid of parameters -> likelihood for each grid param)
    grid: array of params
    
    returns: posterior probablity of each grid param"""
    non_normalized = prior(grid) * likelihood(grid)
    normalization_factor = np.sum(non_normalized)
    return non_normalized / normalization_factor