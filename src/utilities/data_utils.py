r"""
data_utils.py

Utilities for processing of Data
"""
import torch

class CustomCollate:
    r"""
    Override the __call__ method of this collate function
    """

    def __init__(self):
        super(CustomCollate, self).__init__()
        
    
    def __class__(self, batch):
        r"""
        Make changes to the batch of input, useful for tokenizing/padding on the fly

        Args:
            batch (torch.Tensor): A batch of batch_len will come here from torch.util.Dataset
        """
        raise NotImplementedError("Collate function is not implemented")
        
        x = batch[0]
        y = batch[1]
        return x, y