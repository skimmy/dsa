import heapq

def tree2code(r):
    pass

# Node is a tuple (frequency, characters, left, right)
def encode(f):
    n = len(f)
    q = []
    for k, v in f.items():
        heapq.heappush(q, (v,k, None, None))
    for i in range(n-1):
        n1 = heapq.heappop(q)
        n2 = heapq.heappop(q)
        nn = (n1[0] + n2[0], f"{n1[1]},{n2[1]}", n1, n2)
        heapq.heappush(q, nn)
    root = heapq.heappush(q)    
    return tree2code(root)

def main():
    f = {
        "A": 0.34,
        "B": 0.14,
        "C": 0.12,
        "D": 0.06,
        "E": 0.19,
        "F": 0.15
    }
    codebook = encode(f)
    print(codebook)

        
if __name__ == "__main__":
    main()