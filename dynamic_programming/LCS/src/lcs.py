def lcs(x,y):
    """Computes the longest common subsequence between x and y returning its
    length and the whole dynamic programming matrix."""
    n = len(x)
    m = len(y)
    # using only * won't work (all rows will be be the same object)
    matrix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                matrix[i][j] = max(
                    matrix[i-1][j-1]+1,
                    matrix[i][j-1],
                    matrix[i-1][j]
                )
            else:
                matrix[i][j] = max(
                    matrix[i-1][j],
                    matrix[i][j-1],
                    matrix[i-1][j-1]
                )
    return matrix[n][m], matrix

    

def main():
    test = [
        ("race", "aca"),
        ("abac", "aba")
    ]
    for x,y in test:
        l, m = lcs(x, y)
        s = sum([sum(r) for r in m])
        print(f"LCS({x},{y}) = {l} (Sum = {s})")
    
    

if __name__ == "__main__":
    main()