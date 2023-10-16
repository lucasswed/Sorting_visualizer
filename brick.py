def brick_sort(a):
    n = len(a)
    is_sorted = False
    while not is_sorted:
        # Even indexes
        for i in range(0, n-1, 2):
            yield a, [i], [], []
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

                is_sorted = False
        
        # Assume that is sorted
        is_sorted = True

        # Odd indexes
        for i in range(1, n-1, 2):
            yield a, [], [i+1], []
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
