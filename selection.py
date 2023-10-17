def selection_sort(a):
    n = len(a)
    
    for i in range(0, n-1):
        index_smallest = i
        for j in range(i, n):
            yield a, list(range(0,i)), [j], [index_smallest]
            
            if a[j] < a[index_smallest]:
                index_smallest = j
        a[i], a[index_smallest] = a[index_smallest], a[i]