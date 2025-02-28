def merge(a1, a2):
    a = [None]*(len(a1)+len(a2))
    i1 = 0
    i2 = 0
    j = 0
    while (i1 < len(a1)) and (i2 < len(a2)):
        if a1[i1] < a2[i2]:
            a[j] = a1[i1]
            i1 += 1
        else:
            a[j] = a2[i2]
            i2 += 1
        j += 1
    while i1 < len(a1):
        a[j] = a1[i1]
        i1 += 1
        j += 1
    while i2 < len(a2):
        a[j] = a2[i2]
        i2 += 1
        j += 1
    return a    
    

def mergesort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a1 = mergesort(a[:m])
    a2 = mergesort(a[m:])
    return  merge(a1,a2)
    

def main():
    A = [8,7,6,5,4,3,2,1]
    
    A = mergesort(A)
    print(A)
    
    

if __name__ == "__main__":
    main()