def strassen(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
    
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]

    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    return [
        [p5 + p4 - p2 + p6, p1 + p2],
        [p3 + p4, p1 + p5 - p3 - p7]
    ]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = strassen(A, B)
print("Product Matrix:", result)
