def reverseDigits(num):
    rev = 0
    while num>0:
        rev = rev * 10 + num % 10
        num = num//10
    return rev
def isPalindrome(num):
    rev_num = reverseDigits(num)
    if rev_num == num:
        return True

    return False

num = 121
print(isPalindrome(num))