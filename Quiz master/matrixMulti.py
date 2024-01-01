def multiplyMatrices(A, B):
    C = []
    for a in range(len(A[0])):
        C.append([])
        for b in range(len(B[0])):
            C[] = sum([A[a][i]*B[i][b] for i in range(len(A[a]))])
