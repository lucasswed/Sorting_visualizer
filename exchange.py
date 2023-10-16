def exchange_sort(a):
    n = len(a)
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                yield a, [i], [j], list(range(0, i))
