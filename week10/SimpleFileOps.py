filename = "demo.txt"

f = open(filename, "r")
line = f.readline().rstrip("\n")
while line:
    print(line)
    line = f.readline().rstrip("\n")
