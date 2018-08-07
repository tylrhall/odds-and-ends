
import numpy as np
import scipy.stats as st
from statsmodels.distributions.empirical_distribution import ECDF

def inverse_transform_sampling_in(mean, variance, size):# 
    data = np.random.normal(mean, variance, size)# this data gives us the cdf to calculate the quantile from
    zeroToOne = st.norm.cdf(data) #calculates the quantile from original data
    inv_cdf = st.norm.ppf(zeroToOne) #uses the probability distribution function to calculate value
    return inv_cdf

def inverse_transform_sampling_out(data, mean, variance, size):
    toFit = np.random.normal(mean, variance, size)
    zeroToOne = ECDF(data)(data)
    values = np.percentile(toFit, zeroToOne*100)
    return values