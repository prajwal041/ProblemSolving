import collections
import sys
s= "abppplee"
d= {"able","ale","apple","bale","kangaroo"}

def find_longest_subsequence_v1(S, D):
    """ Greedy Algorithm """
    D = sorted(D, key=len, reverse=True)
    for word in D:
        i = j = 0
        while True:
            try:
                i = S[i:].index(word[j])
                print(i)
                j+=1
            except ValueError:
                break
            except IndexError:
                return word

print(find_longest_subsequence_v1(s,d,))

