def sumlist(l):
    if l == []:
        return 0
    else:
        first = l[0]
        rest = l[1:]
        return first + sumlist(rest)
       #return l[0] + sumlist(l[1:)
       #shorter code
    
print(sumlist([1, 4, 13, 34, 56]))

def maxlist(l):
    if len(l) == 1:
        return l[0]
    
    else:
        a = maxlist(l[1:])
        return a if a > l[0] else l[0]
    
    
    

print(maxlist([2, 13, 5, 7, 8]))