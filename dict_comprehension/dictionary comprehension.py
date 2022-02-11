# """wap to create dictionary of words and it's count"""
string_ = 'kasi learns python and kasi id from guntur'
words = string_.split()
# d = {}
# for word in words:
#     if word not in d:
#         d[word] = 1
#     elif word in d:
#         d[word] += 1
# print(d)

# string_ = 'kasi learns python and kasi id from guntur'
# words = string_.split()
# d = {}
# for word in words:
#     d[word] = string_.count(word)
# print(d)


# dict_ = {word: words.count(word) for word in words}
# print(dict_)
#
# list_ = ['kasi','python']
# def sam(string_):
#     return [string_]
# res = map(sam, list_)
# print(list(res))



# """to crete a dictionary word and it's count pair only if the word is of even lenth"""
#
# string_ = 'kasi nadh kasi kasi'
# words = string_.split()
# d = {}
# for word in words:
#     if len(word) % 2 == 0:
#         d[word] = words.count(word)
#
# print(d)
#
# dd = {word:words.count(word)}
# print(dd)

# list_ = [1,2,3,4,5]
# def sqr(item):
#     index,item = item
#     return [item**index]
#
#
# res = map(sqr, enumerate(list_))
# print(list(res))


list_ = [1,2,3,4,5]


res = lambda item:  item[1]**item[0]
print(list(map(res, enumerate(list_))))





