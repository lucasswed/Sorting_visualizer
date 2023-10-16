def gnome_sort(a):
    n = len(a)
    i = 0
    while i < n:
        
        # go right if the current array element is greater then the previous one
        # or if we are at the start
        if a[i] > a[i-1] or i == 0:
            yield a, [i], [], []
            i += 1
        # else: make a swap and go left
        else:
            yield a, [], [i], []
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
        