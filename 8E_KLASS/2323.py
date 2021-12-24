def f(n):
    if n == 0:
        return 1
    return f(n - 1) * 3

print(f(4))
