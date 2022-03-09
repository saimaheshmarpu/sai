# done by sai mahesh
import numpy as np

vector = np.array([1,4,3,2,0])
print("Given vector")
print(vector)
a = 5
new_vector = np.zeros(len(vector) + (len(vector)-1)*(a))
new_vector[::a+1] = vector
print("\nNew vector:")
print(new_vector)