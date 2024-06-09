import random
import math

def calculate_loss():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    
    num_samples = int(num_samples)
    
    loss_name = input("Input loss name (MAE, MSE, RMSE): ")
    
    if loss_name not in ["MAE", "MSE", "RMSE"]:
        print(f"{loss_name} is not supported")
        return
    
    predictions = []
    targets = []
    losses = []

    # Generate predictions and targets
    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predictions.append(pred)
        targets.append(target)
        
        if loss_name == "MAE":
            loss = abs(pred - target)
        elif loss_name == "MSE":
            loss = (pred - target) ** 2
        elif loss_name == "RMSE":
            loss = (pred - target) ** 2
        
        losses.append(loss)
        
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
    
    # Calculate final loss
    if loss_name == "MAE":
        final_loss = sum(losses) / num_samples
        print(f"final MAE: {final_loss}")
    elif loss_name == "MSE":
        final_loss = sum(losses) / num_samples
        print(f"final MSE: {final_loss}")
    elif loss_name == "RMSE":
        final_loss = math.sqrt(sum(losses) / num_samples)
        print(f"final RMSE: {final_loss}")

# Call the function
calculate_loss()