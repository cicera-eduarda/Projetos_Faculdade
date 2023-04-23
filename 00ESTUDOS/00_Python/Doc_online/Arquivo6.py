def fib2(n):
    """"Return a list containig the Fibonacci series up to n."""
    result = []
    a, b = 0 , 1 
    while a < n:
        result.append(a)
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

        ## Não funciona olha que alegria