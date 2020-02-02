from itertools import combinations
def getCountOfPossibleTeams(coders):
    combs = []
    for i in range(1, len(coders) + 1):
        combs.append(i)
        els = [list(x) for x in combinations(coders, i) if len(x)==3]
        for i in els:
           return all(i > i[x+1]>i[x+2] for x in els)
            # for p in i:
            #     print(p)
        # if len(els)==3:
    #     combs.append(els)
    # print(combs)

coders = [5,2,3,1,4]
getCountOfPossibleTeams(coders)