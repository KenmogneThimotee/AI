import torch.nn as nn
import torch
import sys

s = nn.Sequential(
    nn.Linear(3, 4),
    nn.ReLU(inplace=True),
    nn.Linear(4, 5),
    nn.ReLU(inplace=True),
    nn.Dropout(p=0.3),
    nn.Softmax(dim=1)
)

print(s(torch.FloatTensor([[3, 5, 20]])))
