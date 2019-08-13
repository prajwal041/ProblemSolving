n = input()
arr = list(map(int, input().split()))

def countbit(n):                                    # T ~ O(n)
    count = 0
    while(n):
        if(n & 1):
            count+=1
        n=n>>1
    return(count)

def partition(arr,aux,low,high):                    # T ~ O(nlogn)
    i = low-1
    pivot = aux[high]

    for j in range(low,high):
        if aux[j]<=pivot:
            i+=1
            aux[i],aux[j]=aux[j],aux[i]
            arr[i],arr[j]=arr[j],arr[i]
    aux[i+1],aux[high]=aux[high],aux[i+1]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)

def quicksort(arr,aux,low,high):                    # T ~ O(k)
    if low <high:
        pi = partition(arr,aux,low,high)
        quicksort(arr,aux,low,pi-1)
        quicksort(arr,aux,pi+1,high)

def cardnalitysort(arr):                            # T ~ O(n)+O(k)+O(nlogn)+ O(n)
    n = len(arr)
    aux = [0 for i in range(n)]
    for i in range(0,n):
        aux[i] = countbit(arr[i])
    quicksort(arr,aux,0,n-1)
    print(aux)
    return(arr)

result = cardnalitysort(arr)
print(result)

'''
Overall Time T ~ O(nlogn)
'''