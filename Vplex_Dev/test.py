import re
li = ['MozillaFirefox-60.7.0esr-78.40.2.x86_64.rpm']
print(re.findall(r"[\w']+", li[0]))
