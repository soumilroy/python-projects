def fibbonaci(n):
    a, b, = 0, 1
    print(f"""Print a Fibonacci series up to {n}.""")

    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fibbonaci(1000)
fibbonaci(2000)
