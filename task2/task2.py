import sys
 
with open(file = sys.argv[1], mode = "r", encoding = "utf-8") as f:
    list=f.readlines()
    list1=[int (x) for x in list]
m = sorted(list1)[len(list1) // 2]
print(sum(abs(v - m) for v in list1))