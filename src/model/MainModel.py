""" 
Write your main Model here
"""
import torch
import torch.nn as nn


class MainModel(nn.Module):
    def __init__(self, hparams):
        super(MainModel, self).__init__()

        # raise NotImplementedError("Change this model definition to your model definitiion")
        self.layer = nn.Linear(20,  1)

    def forward(self, x):
        return self.layer(x)
