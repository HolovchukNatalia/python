def product_of_even_or_odd(N):
    product = 1
    if N % 2 == 1:  
        for i in range(1, N + 1, 2):
            product *= i
    else:  
        for i in range(2, N + 1, 2):
            product *= i
    return product
