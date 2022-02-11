#local variable
# a=10
# def spam():
#     global a
#     a=a+5
#     print(a)
# spam()
# print(a)
# def spam():
#     a=10
#     print(a)
# spam()
# print(a)


def f1():
    x=10
    def f2():
        nonlocal x
        x+=2
        print(x)
    f2()
f1()
u