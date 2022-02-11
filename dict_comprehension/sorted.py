'''default sorting the collection data tyepes'''
# s="hello"
# print(sorted(s))

# l = [5, 4, 8, 6, 1, 9, 11, 7]
# l.sort()
# print(l)
'''sorting based on the lentgh of the elements'''
l=["python","java","c","ruby","perl","hana"]
print(sorted(l, key=len))
print(sorted(l))
print(sorted(l,key=len,reverse=True))
def s(i):
    d = sorted(i)
    c = sorted(d, key= len)
    return c
print(sorted(l, key = len, reverse=True))

# d = {"gmail": 5, "apple": 3, "walmart": 7, "flipkart": 8}
# print(sorted(d, reverse=True))
# print(sorted(d.items()))

