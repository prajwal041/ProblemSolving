import re
import sys

q = ''.join(sys.stdin.readlines())
if 'java' in q:
    print("Java")
elif '#include' in q:
    print("C")
else:
    print("Python")