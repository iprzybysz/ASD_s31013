def insertion_sort(arr: list[int]):
    for next in range(1, len(arr)):
        curr = next
        temp = arr[next]
        
        while curr > 0 and temp < arr[curr - 1]:
            arr[curr] = arr[curr - 1]
            curr -= 1
            
        arr[curr] = temp
    
    return arr


def merge_sort(S: list[int]):
    if len(S) <= 1:
        return S
    
    m = len(S) // 2 
    
    left = merge_sort(S[:m])
    right = merge_sort(S[m:])
    
    return merge(left, right)


def merge(a1, a2):
    i = j = 0
    result = [] 
    
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1
    
    while i < len(a1):
        result.append(a1[i])
        i += 1
    
    while j < len(a2):
        result.append(a2[j])
        j += 1
    
    return result


def quicksort(a, l, r):
    if l >= r:
        return
    
    k = partition(a, l, r)
    quicksort(a, l, k - 1)   
    quicksort(a, k + 1, r)  


def partition(a: list[int], l: int, r: int):
    i = l + 1
    j = r
    p = a[l]  
    
    while True:
        while i < r and a[i] <= p:
            i += 1
            
        while j > i and a[j] >= p:
            j -= 1
            
        if i < j:
            a[i], a[j] = a[j], a[i]  
        else:
            break
    
    if a[i] > p:
        a[l] = a[i - 1]
        a[i - 1] = p
        return i - 1
    else:
        a[l] = a[i]
        a[i] = p
        return i
