from itertools import combinations
string1,n12=map(int,input().split())
n21=len(str(string1))
a12=list(combinations(str(string1),n21-n12))
a12=(sorted(a12))
b12="".join(a1[0])
print(b12)
