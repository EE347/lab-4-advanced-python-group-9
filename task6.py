import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

# Your code goes here
for row in range(6):
    for col in range(6):
        x[row+1,col+1]=0

print('After:') 
print(x)