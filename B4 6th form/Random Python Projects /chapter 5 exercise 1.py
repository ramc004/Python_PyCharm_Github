#1
alist = []
alist.append("apple")
print ("alist =",alist)

blist = [0] *20
print("blist =",alist)

clist = alist + blist
print("clist 2",clist)

lastC = clist.pop()
print("lastC",lastC)
