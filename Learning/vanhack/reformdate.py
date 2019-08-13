import re
from datetime import datetime
def reformadate(dateslist):
    # dates = '20th Oct 1952'
    reformlist = []
    for dates in dateslist:
        if 'th' in dates:
            dates = re.sub('th', '', dates)
        elif 'rd' in dates:
            dates = re.sub('rd', '', dates)
        elif 'nd' in dates:
            dates = re.sub('nd', '', dates)
        elif 'st' in dates:
            dates = re.sub('st', '', dates)
        struct_time = datetime.strptime(dates, "%d %b %Y").date()
        # print(struct_time)
        reformlist.append(str(struct_time))
    return reformlist

n = int(input().strip())
dates = []
for _ in range(n):
    item = input()
    dates.append(item)
print(reformadate(dates))
