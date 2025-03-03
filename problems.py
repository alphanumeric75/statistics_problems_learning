''' 
1️⃣ Bayesian Inference Problem
A factory produces widgets, and the probability of a widget being defective is 5%. A test is performed to check whether a widget is defective. Given the following probabilities:

P(Defective) = 0.05
P(Not Defective) = 0.95
P(Test Positive | Defective) = 0.90 (90% of defective widgets test positive)
P(Test Positive | Not Defective) = 0.02 (2% of non-defective widgets test positive)
Find:
P(Defective | Test Positive) — the probability that a widget is actually defective given that it tested positive.

2️⃣ Hypothesis Testing (Permutation Test)
We have two groups of data representing test scores:

Group A: [75, 80, 88, 90, 85, 78, 82]
Group B: [82, 85, 91, 92, 89, 86, 88]

We want to determine if there is a significant difference in the means of these two groups using a permutation test.

Null Hypothesis (H₀): There is no significant difference in the means of the two groups.
Alternative Hypothesis (H₁): There is a significant difference in the means of the two groups.
Perform 10,000 permutations and calculate the p-value.
If p < 0.05, reject the null hypothesis.
3️⃣ Markov Chain Monte Carlo (MCMC) using Metropolis-Hastings
We aim to generate samples from a target probability distribution, which follows a normal distribution:

True Mean (μ) = 170
True Standard Deviation (σ) = 10
We use the Metropolis-Hastings algorithm to generate 1,000 samples, with a proposal distribution having standard deviation = 12.
''' 
