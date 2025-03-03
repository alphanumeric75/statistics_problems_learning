import numpy as np 

def bayesian_optimization(new_data_points, stds): 
    ''' 
    Bayesian Update using Gaussian Distribution
    1. Generate random prior (mean_0, sigma_0)
    2. Update belief using new data points and standard deviations
    3. Compute updated mean and standard deviation 
    '''

    new_stds = [] 
    new_means = [] 

    # Initialize prior values (randomized)
    sigma_0 = np.random.uniform(1, 10)  # Prior variance (random)
    mean_0 = np.random.uniform(20, 100)  # Prior mean (random)

    # Iterate over data points
    for x_t, sigma_t in zip(new_data_points, stds): 
        # Update formulas
        updated_mean = ((sigma_0 * x_t) + (mean_0 * sigma_t)) / (sigma_0 + sigma_t)
        updated_std = (sigma_t * sigma_0) / (sigma_t + sigma_0)

        # Append results
        new_means.append(updated_mean)
        new_stds.append(updated_std)

        # Update priors for next iteration
        mean_0 = updated_mean
        sigma_0 = updated_std  

    return new_means, new_stds

# Example Usage
new_data_points = [120, 115, 130, 140]  # New observations
stds = [10, 8, 12, 15] 

updated_means, updated_stds = bayesian_optimization(new_data_points, stds) 
print(updated_means) 
print(updated_stds) 
