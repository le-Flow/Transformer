import torch
import torch.nn as nn
import math

class InputEmbeddings(nn.Module):
    # d_model is the dimension of the model
    def __init__(self, d_model: int, vocab_size: int): # Constructor: sets Dimensions of the model
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(self.vocab_size, self.d_model) # setting the Embedding size to 512
        
    # x is a tensor (multi-dimensional array) of input IDs
    def forward(self, x): # PyTorch's Embedding layer maps Input IDs to their corresponding embedding vectors² (Word Vectors)
        return self.embedding(x) * math.sqrt(self.d_model)