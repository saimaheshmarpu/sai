# done by sai mahesh marpu




import numpy as np  
arr1 = np.array([1,2,3,4,5])
i=0
print("enter the numbers of vector 1")
while i<=4:
    arr1[i] = input(": ")
    i=i+1
    
    arr2=np.array([1,2,3,4,5])
    print("enter the numbers of vector 2")
    k=0
    while k <= 4:
        arr2[k] = input ("> ")
        k = k+1
        print(np.allclose(arr1, arr2))