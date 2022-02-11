import csv
# path=r"C:\Users\Kalyan\PycharmProjects\Alpha_3\files_directory\csv_files\employees.csv"
# with open(path) as file:
#     r_obj=csv.reader(file)
#     header =next(r_obj)
#     d={"male":[],"female":[]}
#     for row in r_obj:
#         if row[1] == "male":
#             d["male"] +=[row[0]]
#         else:
#             d["female"] +=[row[0]]
#     print(d)
#
#

# path=r"C:\Users\Kalyan\PycharmProjects\Alpha_3\files_directory\csv_files\test.csv"
# with open(path) as file:
#     read_obj=csv.DictReader(file)
#     l=list(read_obj)
#     res=sorted(l,key=lambda d:float(d["price"]))
#     print(list(res))
#

path=r"C:\Users\Kalyan\PycharmProjects\Alpha_3\files_directory\csv_files\vaccination_data.csv"
from collections import defaultdict
with open(path) as file:
    r_obj=csv.DictReader(file)
    header=next(r_obj)
    d=defaultdict(list)
    for row in r_obj:
         d[row["DATE_UPDATED"]]+= [(row["COUNTRY"],row["TOTAL_VACCINATIONS"])]
res=sorted(d.items())
print(res[-1])
