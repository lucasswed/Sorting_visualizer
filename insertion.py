def insertion_sort(a):
    n = len(a)
    
    # go forward
    for i in range(1, n):
        #store current array element
        current_element = a[i]
        
        # go backward
        j = i
        while current_element < a[j -1] and j >= 1:
            yield a, [i], [j], []
            # copy over element
            a[j] = a[j-1]
            # step left
            j -= 1
        
        # insert the stored array element
        a[j] = current_element
        yield a, [], [i], [j]