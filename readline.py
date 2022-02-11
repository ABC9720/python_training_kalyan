# path =r"C:\Users\Kalyan\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"
# #      count=0
#      for line in file:
#         for char in line.split()"
# with open(path) as file:
#     count = 0
#     for line in file:
#         count+=1
#         print(count,line)

# with open(path) as file:
#     count  = 0
#     for line in file:
#         t=line.split()
#         for line in t:
#             count = count+1
#         print(count)


# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)
#
# with open(path) as file:
#     count=0
#     for line in file:
#         for char in line:
#             if char==" ":
#                 count +=1
#     print(count)

# with open(path) as file:
#      count=0
#      for line in file:
#         for char in line.split():
#             if char[0] in "aeiouAEIOU":
#                 count+=1
# print(count)

# with open(path) as file:
#     d={}
#     count=0
#     for line in file:
#         for word in line.split():
#
#             d[word]=line.count(word)
#     print(d)




# '''to print nth line in the file'''
# from itertools import islice
# n=3
# with open(path) as file:
#     res= islice(file,0,n)
#     print(list(res))
# '''assignment file handling'''
# from collections import deque
# with open (path) as file:
#     lines=deque (file,8)
#     print(len(list(lines)))
#
path=r"C:\Users\Kalyan\PycharmProjects\Alpha_3\files_directory\txt_log_files\football.txt"
# from itertools import islice
with open(path,encoding="UTF-8") as file:
    countries=[]
    for line in file:
        if line.strip():
            list_=line.split()
            countries.append(list_[1])
    print(countries)


