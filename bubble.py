def bubble_sort(a):
    n = len(a)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                yield a, [j+1], [], list(range(n-i, n))
                
