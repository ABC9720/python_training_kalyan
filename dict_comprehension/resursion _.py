def fibonacci_(n ):
    if n<0:
        print("in valid")
    elif n==0:
        return (0)
    elif n==1:
        return (1)
    else:
        return (fibonacci_(n-1)+fibonacci_(n-2))

n=int(input("enter n:"))
print("fibonacci sreies", end=' ')
for i in range(n):
    print(fibonacci_(i), end=' ')