def minimumBribes(q):
    n = len(q)
    swaps = 0
    for i in reversed(range(n)):
        if q[i]-i>3:
            print("Too chaotic")
            return
        elif q[i]>(i+1):
            swaps+=q[i]-(i+1)
        else:
            if n>q[i]:
                n =q[i]
            elif n!=q[i]:
                swaps+=1

    print(swaps)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)