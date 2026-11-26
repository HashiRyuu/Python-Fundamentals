def same_set(a, b):
    a.sort()
    b.sort()
    newA = []
    newB = []
    
    if len(a) == 0 and len(b) == 0:
        return True
    if len(a) == 0 or len(b) == 0:
        return False
    
    currentA = a[0]
    newA.append(currentA)
    for i in range(1, len(a)):
        if a[i] != currentA:
            newA.append(a[i])
            currentA = a[i]
    
    currentB = b[0]
    newB.append(currentB)
    for i in range(1, len(b)):
        if b[i] != currentB:
            newB.append(b[i])
            currentB = b[i]    
            
    return newA == newB

# or shorter version
#def same_set(a, b):
#    return set(a) == set(b)
