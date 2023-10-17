"""
Works just like insertion sort but with a "gap"
The gap size is determined by a specific gap sequence
There are different gap sequences available

Possible sequences 

-Shell gap sequence: n/2, n/4, n/8, ... , 1

-Hibbard: 1, 3, 7, 15, 31, 63, ... -> in reverse order

-Papernov & Stasevich: 1, 3, 5, 9, 17, 33, 65, ... -> in reverse order

-Knuth: 1, 4, 13, 40, 121, ... -> in reverse order

-Tokuda: 1, 4, 9, 20, 46, 103, ... -> in reverse order

-Sedgewick: 1, 8, 23, 77, 281, ... -> in reverse order

-Ciura gaps: 1170, 701, 301, 132, 57, 23, 10, 4, 1

"""
import math


def shell_gaps(n):
    g, gaps = n // 2, []
    while g > 0:
        gaps.append(g)
        g = g // 2
    return gaps


def hibbard_gaps(n):
    i, g, gaps = 0, 0, []
    while g < n:
        i += 1
        g = 2**i - 1
        gaps.append(g)
    gaps.reverse()
    return gaps


def papernov_stasevich_gaps(n):
    i, g, gaps = 0, 0, [1]
    while g < n:
        i += 1
        g = 2**i + 1
        gaps.append(g)
    gaps.reverse()
    return gaps


def knuth_gaps(n):
    i, g, gaps = 0, 0, []
    while g < n:
        i += 1
        g = (3**i - 1) // 2
        gaps.append(g)
    gaps.reverse()
    return gaps


def tokuda_gaps(n):
    i, g, gaps = 0, 0, []
    while g < n:
        i += 1
        g = math.ceil(1 / 5 * (9 * (9 / 4) ** (i - 1) - 4))
        gaps.append(g)
    gaps.reverse()
    return gaps

def sedgewick_gaps(n):
    i, g, gaps = 0, 0, [1]
    while g < n:
        i += 1
        g = 4**i + 3 * 2**i - 1 + 1
        gaps.append(g)
    gaps.reverse()
    return gaps


def ciura_gaps(n):
    return [11750, 701, 301, 132, 57, 23, 10, 4, 1]


gaps_dict = {
    "shell": shell_gaps,
    "hibbard": hibbard_gaps,
    "papernov": papernov_stasevich_gaps,
    "knuth": knuth_gaps,
    "tokuda": tokuda_gaps,
    "sedgewick": sedgewick_gaps,
    "ciura": ciura_gaps
}

def shell_sort(a, sequence = "shell"):
    n = len(a)
    gaps = gaps_dict.get(sequence)(n)
    for gap in gaps:
        # go forward
        for i in range(gap, n):
            # store current array element
            current_element = a[i]

            # go backward
            j = i
            while current_element < a[j - gap] and j >= gap:
                yield a, [i], [j-gap], []
                # copy over element
                a[j] = a[j - gap]
                # step left
                j -= gap

            # insert the stored array element
            a[j] = current_element
