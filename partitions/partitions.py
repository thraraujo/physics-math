""" 
I want to use Don Knuth algorithm, but I'll reorganize it 
"""

def fn(n):

    if n < 0:
        print("The number needs to be greater or equal to zero")
    if n == 0: 
        a = []

    m = 0
    temp = 0
    a = [0 for j in range(n+1)]
    a[0] = n
    q = m - (n == 1)
    
    while q >= 0: # We write as a generator to simplify the analysis. 

        yield a 
    
        if a[q] == 2:
            a[q] = 1 
            q = q - 1
            m = m + 1

        temp = a[q] - 1 
        a[q] = temp
        n = m - q + 1 
        m = q + 1 
        print(m, n, temp)

        if n <= temp: 
           a[m] = n
           q = m - (n == 1)
           continue

        while (n > temp):
            a[m] = temp 
            m = m + 1 
            n = n - temp 
   
        a[m] = n
        q = m - (n == 1)
        

par = fn(3) 

print(next(par))
print(next(par))
print(next(par))
