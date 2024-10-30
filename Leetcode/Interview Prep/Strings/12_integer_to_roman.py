def integerToRoman(num):
    """
    :param num:
    :return: roman
    Time : O(n): no of integer
    Space: O(1)
    """
    roman = ""
    hashList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
                ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
                ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
    for key, val in reversed(hashList):
        if num // val:
            count = num // val
            roman += key * count
            num = num % val
    return roman

num = 1994
print(integerToRoman(num))