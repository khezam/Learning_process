def multiply(n):
    acc = 1
    while n:
        acc *= n
        n -= 1
    return acc

# multiply(5)

def mul(n, acc):
    if n <= 0:
        return acc
    return mul(n - 1, acc * n)
# mul(5, 1)