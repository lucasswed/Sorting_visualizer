def binary_search(a, key, start, end, position):
    if start == end:
        if a[start] > key:
            return start
        else:
            return start + 1
    elif start > end:
        return start
    else:
        middle = round((start + end)/2)
        if a[middle] < key:
            return binary_search(a, key, middle+1, end, position)
        elif a[middle] > key:
            return binary_search(a, key, start, middle-1, position)
        else:
            return middle



def binary_insertion_sort(a):
    n = len(a)
    
    for i in range(1, n):
        #store the key element
        key = a[i]
        
        #find the correct position
        j = binary_search(a, key, 0, i-1, i)
        
        #insert the key element
        yield a, list(range(0,i)), [j], []
        a[0:n] = a[:j] + [key] + a[j:i] + a[i+1:]
