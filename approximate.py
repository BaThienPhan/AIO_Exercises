import math

# Helper function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function to approximate sin(x)
def approx_sin(x, n):
    sin_x = 0
    for i in range(n):
        sin_x += ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
    return sin_x

# Function to approximate cos(x)
def approx_cos(x, n):
    cos_x = 0
    for i in range(n):
        cos_x += ((-1)**i * x**(2*i)) / factorial(2*i)
    return cos_x

# Function to approximate sinh(x)
def approx_sinh(x, n):
    sinh_x = 0
    for i in range(n):
        sinh_x += (x**(2*i + 1)) / factorial(2*i + 1)
    return sinh_x

# Function to approximate cosh(x)
def approx_cosh(x, n):
    cosh_x = 0
    for i in range(n):
        cosh_x += (x**(2*i)) / factorial(2*i)
    return cosh_x

# Test examples
print(f"approx_sin(x=3.14, n=10) >> {approx_sin(3.14, 10)}")
print(f"approx_cos(x=3.14, n=10) >> {approx_cos(3.14, 10)}")
print(f"approx_sinh(x=3.14, n=10) >> {approx_sinh(3.14, 10)}")
print(f"approx_cosh(x=3.14, n=10) >> {approx_cosh(3.14, 10)}")