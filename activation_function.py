import math

# Check if the input is a number
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def test_activation_functions():
    x = input("Input x value: ")
    
    # Check if x is a number
    if not is_number(x):
        print("x must be a number")
        return
    
    # Convert x to a float
    x = float(x)
    
    print("Input activation function (sigmoid|relu|elu)")
    activation_function = input()
    
    if activation_function == "sigmoid":
        result = 1 / (1 + math.exp(-x))
    elif activation_function == "relu":
        result = max(0, x)
    elif activation_function == "elu":
        alpha = 0.01
        result = x if x > 0 else alpha * (math.exp(x) - 1)
    else:
        print(f"{activation_function} is not supported")
        return
    
    # Print the result
    print(f"Input: {x}")
    print(f"{activation_function.capitalize()}: {result}")

# Call the function
test_activation_functions()