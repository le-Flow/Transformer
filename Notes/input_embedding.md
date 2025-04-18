# Input Embedding
## Overview:
**Where are we?**

![](images/input_embedding/2025-04-16-19-46-15.png)
* Input Embedding allows us to convert a Sentence into a Vector of 512 Dimensions
* in this case: a **Word-vector**

**Example:**

![](images/input_embedding/2025-04-16-18-50-08.png)
* Turn the sentence into a list of **Input IDs**
* An Input ID is a number that correspond  to the position of each word in the vocabulary
* Each of these IDs correspond  to an Embedding (Vector of size 512)

<br>

## Code

* lines 5-15
![](images/input_embedding/2025-04-16-19-49-30.png)

**Missing:**
* Explaining the Equation

<br>

### Next up: [Positional Encoding](positional_encoding.md)
