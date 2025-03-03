''' 1st problem ''' 
def bayesian_inference():
    """
    Given:
    - P(Defective) = 0.05
    - P(Not Defective) = 0.95
    - P(Test Positive | Defective) = 0.90
    - P(Test Positive | Not Defective) = 0.02

    Find: P(Defective | Test Positive)
    """
    p_d = 0.05  # Prior probability of defective
    p_Nd = 0.95  # Prior probability of non-defective
    p_T_Tp = 0.90  # Probability of positive test given defective
    p_N_Tp = 0.02  # Probability of positive test given non-defective

    probability_actually = (p_T_Tp * p_d) / ((p_T_Tp * p_d) + (p_N_Tp * p_Nd))
    
    return probability_actually

print(bayesian_inference())  # Should return the correct probability

''' 2nd solution ''' 

import numpy as np

def permutation_test(list_1, list_2, permutations=10000): 
    """
    Hypothesis Testing using Permutation Test
    - Null Hypothesis (H0): No significant difference between the two groups.
    - Alternative Hypothesis (H1): There is a significant difference.
    - p-value threshold: 0.05
    """
    combined = np.array(list_1 + list_2)
    observed_diff = np.abs(np.mean(list_1) - np.mean(list_2))

    count = 0 
    
    for _ in range(permutations): 
        np.random.shuffle(combined)  # Shuffles in-place
        
        new_group_1 = combined[:len(list_1)] 
        new_group_2 = combined[len(list_1):]

        perm_diff = np.abs(np.mean(new_group_1) - np.mean(new_group_2)) 
        if perm_diff > observed_diff:
            count += 1
    
    p_value = count / permutations
    
    if p_value < 0.05: 
        return 'Reject the null hypothesis (significant difference)' 
    else: 
        return 'Fail to reject the null hypothesis (no significant difference)' 
    
# Test Data
Group_A = [75, 80, 88, 90, 85, 78, 82]
Group_B = [82, 85, 91, 92, 89, 86, 88]

result = permutation_test(Group_A, Group_B)
print(result)  # Expected output: Either reject or fail to reject H0

''' 3nd problem ''' 
import numpy as np
from scipy.stats import norm 

# Target distribution (Normal Distribution)
def target_pdf(x): 
    return norm.pdf(x, loc=170, scale=10)  # True mean = 170, std = 10

# Metropolis-Hastings Algorithm
def metropolis_hastings(num_samples, proposal_std): 
    samples = [] 
    current_sample = 120  # Initial guess
    
    for _ in range(num_samples): 
        proposal = current_sample + np.random.normal(0, proposal_std)  # Gaussian proposal distribution
        
        acceptance_ratio = min(1, target_pdf(proposal) / target_pdf(current_sample))
        
        if np.random.rand() < acceptance_ratio: 
            current_sample = proposal 
        
        samples.append(current_sample) 
    
    return samples 

# Run the MCMC sampling
num_samples = metropolis_hastings(1000, proposal_std=12) 
print(num_samples[:10])  # Print first 10 samples
