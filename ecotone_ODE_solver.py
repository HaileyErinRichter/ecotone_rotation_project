""" Hailey Richter
Biophysics PhD student at the University of Notre Dame
Rotation project with Dr. Dervis Can Vural simulating a generic ecotone situation
Dates 02/03/2025-"""

# libraries imported
import numpy as np

"""Function header: """
def population_change_solver(n,r,s,A):
    n_next = n
    # calculate the new number of individuals per group at the next time step
    for i in range(len(n)-1):
        # there should be a del squared times n[i] but idk how that is not just zero
        n_next[i] += r[i] * n[i]
        for j in range(1,len(n)-1):
            n_next[i] += A[i][j] * s[j] * n[j]
    # change the s vector for next time step
    # possibly change the A matrix for next time step
    return n_next,r,s,A

"""Main"""
# matrix of constants representing interaction dynamics
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
             ])
# vector of how many individuals in each population group
n = np.array([1,2,3])
# vector of rate of change in population when no external force for all populations
r = np.array([4,5,6])
# vector of mutation fitness
s = np. array([7,8,9])

# does this run
n,r,s,A = population_change_solver(n,r,s,A)
print("n: " + str(n))
print("r: " + str(r))
print("s: " + str(s))
print("A: " + str(A))