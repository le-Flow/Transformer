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
    
class PositionalEncoding(nn.Module):
    # seq_len is the max length of the sentence || dropout is the dropout rate (makes the model less overfit)
    def _init_(self, d_model: int, seq_len: int, dropout: float): # the dropout randomly drops neurons so that the model doesnt get too accustomed to the training data
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        self.dropout = nn.Dropout(dropout)
        
        # Create a matrix of shape (seq_len, d_model)
        pe = torch.zeros(seq_len, d_model) # Positional Embedding Vector
        # Create a vector of shape (seq_len, 1)
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1) # Position inside of the Positional Embedding Vector pe
        div_term = torch.exp(0, d_model, 2).float() * (-math.log(10000.0) / d_model) # Equation in positional_encoding.md in log space for numerical stability
        # Apply sin to even positions (First Equation)
        pe[:, 0::2] = torch.sin(position * div_term)
        # Apply cos to odd positions (Second Equation)
        pe[:, 1::2] = torch.sin(position * div_term)
        
        # Add extra dimension so we can use it with many sentences at once for parallelization (Batch of sentences)
        pe = pe.unsqueeze(0) #(1, seq_Len, d_model)
        
        self.register_buffer('pe', pe) # Save current Positional Embedding Vector in the model (one of many Positional Embedding Vector)
    
    # Creating and adding the Positional embedding vector for all Words
    def forward(self, x):
        x = x + (self.pe[:, :x.shap[1], :]).requires_grad_(False)
        return self.dropout(x)
    
class LayerNormalization(nn.Module):
    def _init_(self, eps: float = 10**-6) -> None:
        super().__init__()
        self.eps = eps
        self.alpha = nn.Parameter(torch.ones(1)) # Multiplied
        self.bias = nn.Parameter(torch.zeros(1)) # Added
    