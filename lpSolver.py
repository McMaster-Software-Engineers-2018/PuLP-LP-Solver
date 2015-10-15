# Written By: Shawn Simon
# September 22, 2015.
# LP Solver.

from pulp import *

prob = LpProblem("Q2", LpMaximize)

# Variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
s1 = LpVariable("s1", 0)
s2 = LpVariable("s2", 0)
s3 = LpVariable("s3", 0)

# Objective 
prob += x1 - x2

# Constraints 
prob += x1 + x2 - x3 + x4 <= 4
prob += -x2 + x3 + x4 <= 6
prob += x1 + 2*x4 >= 4


GLPK().solve(prob) 

# Solution
for v in prob.variables():
	print v.name, "=", v.varValue

print "objective=", value(prob.objective)
