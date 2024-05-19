

def pascal_triangle(h):
    triangle = []
    for i in range(h):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        print(" " * (h - i - 1), end="")
        print(*row, sep=" ")


pascal_triangle(5)
