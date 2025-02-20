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
    for i in range(len(n)):
        # there should be a diffusion constant del squared n[i]
        n_next[i] += r[i] * n[i]
        for j in range(len(n)):
            n_next[i] += n[i] * A[i][j] * n[j]
            # update the s value for everybody ([i][j])
            # DOESN'T S NEED TO BE A MATRIX OF SIZE LIKE A?
    return n_next,r,A

"""Main"""
# # vector of mutation fitness
# min_val = 1
# max_val = 10
# num_species = 8
# s = np.random.randint(min_val, max_val, num_species)
#
# # vector of how many individuals in each population group
# n = 100 * np.ones(num_species)
#
# # matrix of constants representing interaction dynamics
# # the A matrix is created from a Gaussian distribution B and the trait fitness vector s
# # in the formula A_ij=(s_i-s_j)M_ij
#
# # Define the shape of the matrix (rows, columns)
# rows, cols = 8,8
#
# # Define the mean (mu) and standard deviation (sigma) of the Gaussian distribution
# mu = 0
# sigma = 1
#
# # Generate the matrix with random values from the Gaussian distribution
# gaussian_matrix = np.random.normal(loc=mu, scale=sigma, size=(rows, cols))
# M = gaussian_matrix
# # bias the gaussian to be more biologically realistic
# D = 10 # weight of bias (D >> 1 to make a negative diagonal)
# M = (M - np.matrix_transpose(M) * D) / 2
# A = np.zeros((rows,cols))
# r = np.zeros(num_species)
# for i in range(rows):
#     for j in range(cols):
#         A[i][j] = (s[i] - s[j]) * M[i][j]
#         # vector of rate of change in population when no external force for all populations
#         # built r based on A matrix and n vector
#         r[i] += (-1) * A[i][j] * n[j]

# # does this run
# n,r,A = population_change_solver(n,r,A)
# print("n: " + str(n))
# print("r: " + str(r))
# print("s: " + str(s))
# print("A: " + str(A))

# it runs but the integers get too large for some reason

# test does this run in general
# the problem has to do with np.array vs [] style array!!!
s = [0.4,0.6,0.2,0.8]
n = [4,4,4,4]
M = [[-10,0.2,0.1,0.3],[0.2,-20,0.5,0],[0.1,0.5,-30,0.1],[0.3,0,0.1,-40]]
A = M
r = np.zeros(4)
for i in range(4):
    for j in range(4):
        # if i != j:
        A[i][j] = (s[i] - s[j]) * M[i][j]
        # vector of rate of change in population when no external force for all populations
        # built r based on A matrix and n vector
        r[i] += (-1) * A[i][j] * n[j]
n,r,A = population_change_solver(n,r,A)
print("n: " + str(n))
print("r: " + str(r))
print("s: " + str(s))
print("A: " + str(A))
# again
n,r,A = population_change_solver(n,r,A)
print("\nn: " + str(n))
print("r: " + str(r))
print("s: " + str(s))
print("A: " + str(A))