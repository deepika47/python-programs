
def sumKFirst(arr, n, k):
    sum = 0
    visited = [False for i in range(n)]
    for i in range(0, n, 1):
    if (visited[i] == True): 
            continue
    count = 1
    for j in range(i + 1, n, 1): 
            if (arr[i] == arr[j]): 
                count += 1
                visited[j] = True
      
    if (count == k): 
        sum += arr[i] 
  
    return sum
if __name__ == '__main__': 
    arr = [9, 9, 10, 11, 8, 8, 9, 8] 
    n = len(arr) 
    k = 3
    print(sumKFirst(arr, n, k))
