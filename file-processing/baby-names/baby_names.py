infile = open("babynames.txt", "r")
outfile1 = open("boynames.txt", "w")
outfile2 = open("girlnames.txt", "w")

containBoyTopTen = []
containGirlTopTen = []

count = 0
line = infile.readline()
while line != "":
    string = line.split()
    
    outfile1.write(string[1] + "\n")
    outfile2.write(string[3] + "\n")
    
    if count < 10:
        containBoyTopTen.append(string[1])
        containGirlTopTen.append(string[3])
        
    count += 1
    
    line = infile.readline()

infile.close()
outfile1.close()
outfile2.close()

print("Top 10 most popular baby boy names for 2011:")
for boy in containBoyTopTen:
    print(boy)

print()

print("Top 10 most popular baby girl names for 2011:")
for girl in containGirlTopTen:
    print(girl)










#sort data verison
infile = open("babynames.txt", "r")

boyList = []
girlList = []

line = infile.readline()

while line != "":
    string = line.split()

    boyName = string[1]
    boyCount = int(string[2].replace(",", ""))

    girlName = string[3]
    girlCount = int(string[4].replace(",", ""))

    boyList.append([boyCount, boyName])
    girlList.append([girlCount, girlName])

    line = infile.readline()

infile.close()

boyList.sort()
girlList.sort()

boyList.reverse()
girlList.reverse()

print("Top 10 most popular baby boy names for 2011:")
for i in range(10):
    print(boyList[i][1])

print()

print("Top 10 most popular baby girl names for 2011:")
for i in range(10):
    print(girlList[i][1])
