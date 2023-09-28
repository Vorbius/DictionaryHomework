import csv
infile=open('sometext.txt','r')
dictionary={}
read = infile.read()
lower = read.lower()
words=lower.split()
for i in words:
    i=i.rstrip(",")
    i=i.rstrip(".")
    if i not in dictionary:
        dictionary[i]=0
    if i in dictionary:
        dictionary[i]=dictionary[i]+1

print(dictionary)


infile.close()