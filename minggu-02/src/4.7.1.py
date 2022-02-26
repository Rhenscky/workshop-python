def fib(n):    # Menulis fibonacci
    """ Mencetak nilai fibonacci ."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Memanggil fungsi yang telah didefenisikan:
fib(2000)