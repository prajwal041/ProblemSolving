"""
Problem: A software library to check whether two version of strings

Algorithm Solution: Identify the given two strings is in the form of Float, integer or pure strings
                    1. check the two strings is a float using Regular Expression
                    2. if step 1) returns None then check for integer else check for goto step 4
                    3. In step 2) if we get ValueError then goto step 6
                    4. Perform normal floating comparision goto step 6
                    5. if we get ValueError in step 4 then either s1 or s2 are strings goto step 6
                    6. perform normal string comparision, where we consider set operation to make sure that characters in
                        strings aren't repeated

Test case 1: s1=1.2    s2=1.1
Output:     1.2  greater than  1.1
Analysis:   Since both are fractional values so normal floating comparision

Test case 2: s1=5    s2=7
Output:     7  greater than  5
Analysis:   Since both are integers so normal integer comparision

Test case 3: s1=Canada    s2=USA
Output:    Canada  greater than  USA
Analysis:  Since both are Strings so count the length of the string, based on that position is decided

Test case 4: s1=abc def ghi    s2=def ghi abc
Output:    abc def ghi  &  def ghi abc  are equal
Analysis:  Since both are Strings, remove the repetition then count the length of the string, based on that position is decided

Test case 5: s1=1.7    s2=VanHack
Output:    VanHack  greater than  1.7
Analysis:  Since s1 is fraction value & s2 is a string then perform normal string comparision

Test case 6: s1=Assignment    s2=227
Output:    Assignment  greater than  227
Analysis:  Since s1 is a string & s2 is a integer then perform normal string comparision

Test case 7: s1=abcd1.47xyz    s2=@x%&^!*#()
Output:    abcd1.47xyz  greater than  @x%&^!*#()
Analysis:  Here we take both special characters & mixed strings as normal strings so perform normal string comparision

Time complexicity:
T ~ O(1)

"""
import re
def check_string_version(s1,s2):
    if re.match("^\d+?\.\d+?$", s1) is None and re.match("^\d+?\.\d+?$", s2) is None:
        # print("Not float")
        try:
            # checking integer
            if int(s1) > int(s2):
                print(s1," greater than ",s2)
            elif int(s1) == int(s2):
                print(s1," & ",s2," are equal")
            else:
                print(s2," greater than ",s1)
        except ValueError:
            # checking strings
            sp1 = len(set(s1))
            sp2 = len(set(s2))
            if int(sp1) > int(sp2):
                print(s1," greater than ",s2)
            elif int(sp1) == int(sp2):
                print(s1," & ",s2," are equal")
            else:
                print(s2," greater than ",s1)
    else:
        try:
            # checking Float no's
            if float(s1) > float(s2):
                print(s1," greater than ",s2)
            elif float(s1) == float(s2):
                print(s1," & ",s2," are equal")
            else:
                print(s2," greater than ",s1)
        except ValueError:
            # checking strings
            sp1 = len(set(s1))
            sp2 = len(set(s2))
            if int(sp1) > int(sp2):
                print(s1," greater than ",s2)
            elif int(sp1) == int(sp2):
                print(s1," & ",s2," are equal")
            else:
                print(s2," greater than ",s1)

s1 = input()
s2 = input()
check_string_version(s1,s2)

