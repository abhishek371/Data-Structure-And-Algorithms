def partition(ar):
    p=ar[0]
    eq,left,right=[],[],[]
    for i in ar:
        if i >= p:
            right.append(i)
        elif i <p:
            left.append(i)
    for t in left:
        print t,  
    for k in right:
        print k,
        
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)