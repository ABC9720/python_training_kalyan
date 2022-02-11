dict_ = {'a':2, 'b':2, 'c':3}
for key in dict_:
    print(key,end=" ")


for key in dict_:
    print(dict_[key],end=" ")


for key in dict_:
    print(dict_.get(key))

for key in dict_.keys():
    print(key)

for value in dict_.values():
    print(value)

for key,value in dict_.items():
    print(key,value)


