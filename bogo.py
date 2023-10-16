import random

def bogo_sort(a):
    is_sorted = False
    n = len(a)
    while not is_sorted:
        # Swap two elements
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        a[i], a[j] = a[j], a[i]
        yield a, [i], [j], []

        # Check if sorted
        is_sorted = True
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                is_sorted = False
                break
