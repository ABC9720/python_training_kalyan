# sentence="python is a programming langueage"
# ss=sentence.split()
# shortest,*rest,longest=sorted(ss,key=len)
# print(longest,shortest)

# d={"def":3,"rak":3,"jaj":4}
# print(dict(sorted(d.items(),key=lambda item:item[0][-1])))
# d={"def":3,"rak":3,"jaj":4}
# print(sorted(d.values()))


'based on the temparature'
temparature=[("delhi",3),("chennai",8),("nellore",4)]
print(sorted(temparature,key=lambda item:item[-1]))



