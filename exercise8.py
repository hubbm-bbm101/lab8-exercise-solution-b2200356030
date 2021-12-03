import sys
file = open(sys.argv[1])
inpt = sys.argv[2]
names = {}

for i in file:
    lst = i[:-1].split(":")
    names[lst[0]] = lst[1].split(",")

for j in inpt.split(","):
    try:
        print("Name = %s\nUniversity = %s\nDepartment = %s\n"%(j,names[j][0],names[j][1]))
    except KeyError:
        print("No record of ‘%s’ was found!\n"%j)
        
        