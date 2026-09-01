def palind(r):
    e = len(r) -1
    s = 0

    while s < e:
        if r[s]!= r[e]:
            return False
        s = s+1
        e = e-1
    return True
tuplex = (1,2,3,3,4,1)

if(palind(tuplex)):
    print("The tuple is a Flip-Flop")

else:
    print("The tuple is not a Flip-Flop")

