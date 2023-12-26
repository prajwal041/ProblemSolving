def isPalindrome(s):
    string = ''.join(letter for letter in s if letter.isalnum()).lower()
    if string == string[::-1]:
        return True
    return False

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))