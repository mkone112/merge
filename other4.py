def msort(l):
    if len(l)>1:
        t=len(l)//2
        it1=iter(msort(l[:t]));x1=next(it1)
        it2=iter(msort(l[t:]));x2=next(it2)
        l=[]
        try:
            while True:
                if x1<=x2: l.append(x1);x1=next(it1)
                else     : l.append(x2);x2=next(it2)
        except:
            if x1<=x2: l.append(x2);l.extend(it2)
            else:      l.append(x1);l.extend(it1)
    return l