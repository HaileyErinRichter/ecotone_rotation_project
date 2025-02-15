""" Hailey Richter
Biophysics PhD student at the University of Notre Dame
Rotation project with Dr. Dervis Can Vural simulating a generic ecotone situation
Dates 02/03/2025-"""

# libraries imported
import numpy as np

"""Function header: """
def population_change_solver(n,r,A):
    n_next = n
    # calculate the new number of individuals per group at the next time step
    for i in range(len(n)-1):
        # there should be a diffusion constant del squared n[i] but idk how that is not just zero
        n_next[i] += r[i] * n[i]
        for j in range(1,len(n)-1):
            n_next[i] += n[i] * A[i][j] * n[j]
    return n_next,r,A

"""Main"""
# matrix of constants representing interaction dynamics
# the A matrix is created from a Gaussian distribution B and the formula
# A = (B - D * B transpose)/2 + the k summation of (C_ij*S_k) where D is much greater than 1

# Define the shape of the matrix (rows, columns)
rows, cols = 8,8

# Define the mean (mu) and standard deviation (sigma) of the Gaussian distribution
mu = 0
sigma = 1

# Generate the matrix with random values from the Gaussian distribution
gaussian_matrix = np.random.normal(loc=mu, scale=sigma, size=(rows, cols))
B = gaussian_matrix

A = (B - 100 * B) / 2

# vector of how many individuals in each population group
n = np.array([1,2,3])
# vector of rate of change in population when no external force for all populations
r = np.array([4,5,6])
# vector of mutation fitness
s = np. array([7])

# does this run
n,r,A = population_change_solver(n,r,A)
print("n: " + str(n))
print("r: " + str(r))
print("s: " + str(s))
print("A: " + str(A))