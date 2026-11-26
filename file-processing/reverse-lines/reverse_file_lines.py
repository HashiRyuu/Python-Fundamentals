infile = open("input.txt", "r")
outfile = open("output.txt", "w")

line = infile.readline()
contain = []
while line != "":
    line.strip()
    contain.append(line)
    line = infile.readline()

for i in range(len(contain) - 1, -1, -1):
    outfile.write(contain[i])
    print(contain[i])



infile.close()
outfile.close()
