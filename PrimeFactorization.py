n=int(input("Enter an integer 2 or greater:"))
print("The Prime Factors are:")
factor=2
while(factor <= n):
    k = 0
    if(n % factor == 0):
        j=1
        while(j <= factor):
            if(factor % j == 0):
                k = k + 1
            j = j + 1
        if(k == 2):
            print(factor)
    factor = factor + 1

