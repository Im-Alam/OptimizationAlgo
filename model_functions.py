
from numpy import arange, meshgrid
from numpy import exp, sqrt, cos, sin, e, pi, absolute
 



# Quadratic function
def quadratic(x):
    return x**2



# Multivariable hammok function
def hammok(x,y):
    return x**2 + y**2

# Multivaruable unimodal function
def objective(x, y):
	return 0.26 * (x**2 + y**2) - 0.48 * x * y
 

# Easoms function
def easom(x, y):
    """
    x: [-10, 10]
    y: [-10, 10]
    optimum at (pi,pi)
    """
    return -cos(x) * cos(y) * exp(-((x - pi)**2 + (y - pi)**2))


# Ackley's function
def ackley(x, y):
    """
    x: [-5,5]
    y: [-5,5]
    optimum: [0,0]
    """
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20
 

# Himmelblau’s function
def Himmelblau(x, y):
    """
    x: [-5,5]
    y: [-5,5]
    optimum value: [3.0, 2.0], [-2.805118, 3.131312], [-3.779310, -3.283186], [3.584428, -1.848126]
    """
    return (x**2 + y - 11)**2 + (x + y**2 -7)**2
 

# Holder’s table function
def Holder(x, y):
    """
    x: [-10,10]
    y: [-10, 10]
    optimum value: [8.05502, 9.66459], [-8.05502, 9.66459], [8.05502, -9.66459], [-8.05502, -9.66459]
    """
    return -absolute(sin(x) * cos(y) * exp(absolute(1 - (sqrt(x**2 + y**2)/pi))))


# Rosenbrock function
def rosenbrock(x,y):
    return (1-x)**2 + 100*((y-x**2)**2)
