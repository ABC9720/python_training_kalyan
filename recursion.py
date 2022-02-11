def fibonacci_(n ):
    if n<0:
        print("in valid")
    elif num==0:
        return (0)
    elif num==1:
        return (1)
    else:
        return (fibonacci_(n-1)+fibonacci_(n-2))

n=int(input())
for i in range(n):
    print(fibonacci_(i))
# res=fibonacci_(n)
# print(fibonacci_((res)))