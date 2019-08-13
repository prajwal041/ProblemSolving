
hash = {}
import itertools
def optimizehours(meeting, hrs):
    for i in range(0,len(meeting)+1):
        for subs in itertools.combinations(meeting, i):
            if sum(subs)<=hrs:
                hash[subs]=hrs-sum(subs)
                # print(hash)
    val = min(hash.values())
    print(list(hash.keys())[list(hash.values()).index(val)])

meeting = [5,2,2]
hrs = 1
optimizehours(meeting,hrs)

'''
T ~ O(n2)
'''