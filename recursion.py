def sum(n):
    
    if n == 0:
        return 0
    
    return n + sum(n-1)




def factorial(n):
    
    if n==1 or n ==0:
        return 1
    
    
    return n * factorial(n-1)








def fibonaci(n):
    
    if n>=0:
        if n <=1:
            return n
        
        return fibonaci(n-1) + fibonaci(n-2)
    
    



def fib(n):
    
    if n<=1:
        print(n)
        return
    
    fib1 = 0
    fib2 = 1
    fib3 = 0
    
    for i in range(n-1):
        
        fib3 = fib1+fib2
        fib1 = fib2
        fib2 = fib3
    
    print(fib3)

fib(0)