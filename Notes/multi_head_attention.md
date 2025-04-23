# Multi Head Attention
## Overview:
**Where are we?**

![](images/multi_head_attention/2025-04-21-16-14-09.png)

## Single Head Self Attention
* Self Attention allows the model to relate each word in a sentence to each other
![](images/multi_head_attention/2025-04-21-17-08-24.png)
* Q = Input Matrix, K = Input Matrix Transposed
* Turns the Matrix into a 6x6 Matrix, with each cell being the dot product of the respective row and column
* Every row sums up to 1
* For example, the cell [your, cat] is the dot product of the embedding of the word your and the embedding of the word cat
* this value shows how intense (likely) the relationship between one word and another is
![](images/multi_head_attention/2025-04-21-17-14-29.png)
* Then we

## Equations
![](images/multi_head_attention/2025-04-21-17-10-39.png)