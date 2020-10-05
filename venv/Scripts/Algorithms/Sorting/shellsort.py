import sys
def shellSort(arr): 
  

    n = len(arr) 
    gap = n//2
  
 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            
            temp = arr[i] 
  
         
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
           
            arr[j] = temp 
        gap //= 2
  
  
 
arr=[]
g = int(input("Enter number of elements : ")) 
  
for i in range(0, g): 
    ele = int(input()) 

    arr.append(ele) 

  
n = len(arr) 
print ("Array before sorting:") 
for i in range(n): 
    print(arr[i]), 
  
shellSort(arr) 
  
print ("\nArray after sorting:") 
for i in range(n): 
    print(arr[i]), 