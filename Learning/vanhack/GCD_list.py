def GCD(a, b):
    """ The Euclidean Algorithm """
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b % a, a
    return b


def GCD_List(list):
    """ Finds the GCD of numbers in a list.
    Input: List of numbers you want to find the GCD of
        E.g. [8, 24, 12]
    Returns: GCD of all numbers
    """
    GCD = 1
    for i in range(len(list)):
        p = list[i]
        k=0
        while(k<len(list)):
            if p%list[k]:
                GCD=p
                k+=1
    return GCD
list =[2,4,6,8]
print(GCD_List(list))