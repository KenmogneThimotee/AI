import torch.nn as nn
import torch


L = nn.Linear(2, 5, bias=True)

v = torch.FloatTensor([3, 5])

print(L(v))
