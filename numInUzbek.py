baza={1 : "bir ",
      2 : "ikki ",
      3 : "uch ",
      4 : "to'rt ",
      5 : "besh ",
      6 : "olti ",
      7 : "yetti ",
      8 : "sakkiz ",
      9 : "to'qqiz ",
      10 : "o'n ",
      20 : "yigirma ",
      30 : "o'ttiz ",
      40 : "qirq ",
      50 : "ellik ",
      60 : "oltmish ",
      70 : "yetmish ",
      80 : "sakson ",
      90 : "to'qson ",
      100 : "yuz ",
      1000 : "ming ",
      1000000 : "million ",
      1000000000 : "milliard "
      }

a=list(input())
c=len(a)
res=""
nol=0
nolm=0
if 1<=c<=3:
    if c%3==0:
        for i in range(3):
            if int(a[i])==0:
                continue
            else:
                if i==1:
                    res+=baza[int(a[i])*10] 
                else: 
                    res+=baza[int(a[i])]
                if i==0:
                    res+=baza[100]
    if c%3==2:
        for i in range(2):
            if int(a[i])==0:
                continue
            else:
                if i==0:
                    res+=baza[int(a[i])*10] 
                else: 
                    res+=baza[int(a[i])]
    if c%3==1:
        i=0
        res+=baza[int(a[i])]
    print(res)
if 3<c<=6:
    for q in range(2):
        if q==0:
            z=0
        if c%3==0:
            for i in range(3):
                if int(a[i+z])==0:
                    continue
                else:
                    if i==1:
                        res+=baza[int(a[i+z])*10] 
                    else: 
                        res+=baza[int(a[i+z])]
                    if i==0:
                        res+=baza[100]
            z=3
        if c%3==2:
            for i in range(2):
                if int(a[i])==0:
                    continue
                else:
                    if i==0:
                        res+=baza[int(a[i])*10] 
                    else: 
                        res+=baza[int(a[i])]
            z=2
            c-=2
        if c%3==1:
            res+=baza[int(a[0])]
            c-=1
            z=1
        if q==0:
            res+=baza[1000]
    print(res)
if 6<c<=9:
    for q in range(3):
        if q==0:
            z=0
        if c%3==0:
            for i in range(3):
                if int(a[i+z])==0:
                    if q==1:
                        nol+=1
                    continue
                else:
                    if i==1:
                        res+=baza[int(a[i+z])*10] 
                    else: 
                        res+=baza[int(a[i+z])]
                    if i==0:
                        res+=baza[100]
            if q==0 or q==1:
                z+=3
        if c%3==2:
            for i in range(2):
                    if i==0:
                        res+=baza[int(a[i])*10] 
                    else: 
                        res+=baza[int(a[i])]
            c-=2
            z=2
        if c%3==1:
            res+=baza[int(a[0])]
            c-=1
            z=1
        if q==0:
            res+=baza[1000000]
        if q==1:
            if nol!=3:
                res+=baza[1000]
    print(res)
if 9<c<=12:
    for q in range(4):
        if q==0:
            z=0
        if c%3==0:
            for i in range(3):
                if int(a[i+z])==0:
                    if q==1:
                        nolm+=1
                    if q==2:
                        nol+=1
                    continue
                else:
                    if i==1:
                        res+=baza[int(a[i+z])*10] 
                    else: 
                        res+=baza[int(a[i+z])]
                    if i==0:
                        res+=baza[100]
        if q==0 or q==1 or q==2:
            z+=3
        if c%3==2:
            for i in range(2):
                    if i==0:
                        res+=baza[int(a[i])*10] 
                    else: 
                        res+=baza[int(a[i])]
            c-=2
            z=2
        if c%3==1:
            res+=baza[int(a[0])]
            c-=1
            z=1
        if q==0:
            res+=baza[1000000000]
        if q==1:
            if nolm!=3:
                res+=baza[1000000]
        if q==2:
            if nol!=3:
                res+=baza[1000]
    print(res)