import torch
import torch.nn as nn
import torch.nn.functional as F

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        return F.softmax(x, dim=0)

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_val = torch.max(x)
        exp_x = torch.exp(x - max_val)
        return exp_x / torch.sum(exp_x)

# Example 1
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print("Softmax output:", output)  # Expected: tensor([0.0900, 0.2447, 0.6652])

# Example 2
data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print("SoftmaxStable output:", output)  # Expected: tensor([0.0900, 0.2447, 0.6652])