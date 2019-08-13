def solution(s,p,q):
    result =[]
    DNA_len = len(s)
    mapping = {"A":1,"C":2,"G":3,"T":4}
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len,[-1]*DNA_len,[-1]*DNA_len]
    next_nucl[mapping[s[-1]]-1][-1] = DNA_len-1
    for i in range(DNA_len-2,-1,-1):
        next_nucl[0][i]=next_nucl[0][i+1]
        next_nucl[1][i]=next_nucl[1][i+1]
        next_nucl[2][i] = next_nucl[2][i + 1]
        next_nucl[3][i] = next_nucl[3][i + 1]
        next_nucl[mapping[s[i]]-1][i]=i
    for i in  range(len(p)):
        if next_nucl[0][p[i]]!=-1 and next_nucl[0][p[i]]<=q[i]:
            result.append(1)
        elif next_nucl[1][p[i]] != -1 and next_nucl[1][p[i]] <= q[i]:
            result.append(2)
        elif next_nucl[2][p[i]] != -1 and next_nucl[2][p[i]] <= q[i]:
            result.append(3)
        else:
            result.append(4)
    return result

s="CAGCCTA"
p=[2,5,0]
q=[4,5,6]
print(solution(s,p,q))