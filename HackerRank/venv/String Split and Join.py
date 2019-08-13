def splitjoin(line):
    line = line.split()
    line = "-".join(line)
    return(line)

line = splitjoin(input())
print(line)