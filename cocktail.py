def cocktail_sort(a):
    n = len(a)
    is_sorted = False
    start, end = 0, n-1
    while not is_sorted:
        # Forward pass
        is_sorted = True
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
                yield a, [i+1], list(range(0, start)), list(range(end+1, n))
 
        # update end
        end -= 1
        
        # Check if done
        if is_sorted:
            break

        # Backward pass
        is_sorted = True
        for i in range(end-1, start-1, -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
                yield a, [i], list(range(0, start)), list(range(end+1, n))
        
        #update start
        start += 1
        
