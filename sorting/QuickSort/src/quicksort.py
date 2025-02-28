def partition(A,p,q):
    pivot = A[q]
    i = p - 1
    for j in range(p,q-1):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j] # swap
    A[i+1], A[q] = A[q], A[i+1] # place the pivot
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def main():
    A = [4,2,7,2,8,0]
    print(A)
    partition(A,0,len(A)-1)
    print(A)
    
    quicksort(A,0,len(A)-1)
    print(A)

if __name__ == "__main__":
    main()