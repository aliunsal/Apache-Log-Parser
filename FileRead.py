from datetime import time

__author__ = 'aliunsal'

from collections import Counter
import time
import  fileinput

position = 0
last = ""
# while last != "\n":
#     last = file.readline()
#     print last
#     position += len(file.readline())
#     file.seek(position)
#

# def file_read(file):
#     for line in file:
#         l = line.split(" ")
#         yield l[6]

file = fileinput.input("test.log")

for line in open("test.log", "r"):
    print line


# link = []
#
# with open("test.log", "r") as file:
#     start = time.time()
#     for f in file:
#         s = f.split(" ")
#         try:
#             link.append(s[6])
#         except:
#             print("")
#     end = time.time() - start
#     print end
#
# print "%s %d adet istek yapilmistir" % Counter(link).most_common(1)[0]