def compute_threshold(epsilon):
    ceiling = math.ceil
    x = pow(e,0.5)
    y = (1+1/epsilon)
    z = math.pow(y,2)
    e_value = math.pow(e,0.5)
    final=3*e*z
    P = int(ceiling(final)) 

def computeiter_count(delta):
    ceiling = math.ceil
    ln = math.log
    a = 3/delta
    result = 35*ln(a)
    R= int(ceiling(result))


def find_median(c):

    if not c:    
        return 0
    else:
        srt = sorted(c)
        print (srt)
        leng = len(srt)
        if not leng % 2:
            return int((srt[ leng / 2 ] + srt[ leng / 2 - 1]) / 2.0 )   # // is used in newer versions of python
        return int(srt[ leng / 2 ] )



def ApproxMcCore(F,pivot):
    S = BoundedSAT(F,pivot+1)
    if (|S|<=pivot)
    return |S|
    else
    floor = math.flr
    ln = math.log
    
    l = int(floor*ln(pivot)-1)
    i=l-1
    while (1<=S<=pivot) or (i=n)
    i=i+1
    h=(n,l-3,3)
    alpha={0,1}i-l
    S=BoundedSAT(f----)
    if ((S>pivot) or S=0)
       return null
    else
        k = math.pow(2,i-1)
        return k
         
    
    

    
