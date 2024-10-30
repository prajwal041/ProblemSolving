def colorList(s):
    d = {}
    str = s.split(" ")
    for item in str:
        key, val = item[-1], item[:-1]
        d[key] = val
    print(d)
    color = ""
    sorted_d = sorted(d.keys())
    for key in sorted_d:
        color += d[key] + " "
    print(color)

input = "red2 blue5 black4 green1 gold3"
colorList(input)