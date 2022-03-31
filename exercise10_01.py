#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

#use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File does not exist:', fname)
    quit()
#create dictionary and lists
counts = dict()
lst = list()
newlst = list()
#go through lines
for line in fh:
    if len(line) < 1:
        continue
    if line.startswith('From '):
        linesplit = line.split()
        #isolate email
        email = linesplit[1:2]
    for e in email :
        counts[e] = counts.get(e,0) + 1
t = sorted(counts.items())
#sorted by key, value
for k, v in sorted(counts.items()) :
    print(k,v)

#sorted by value, key
print("Sorted by low to high:", sorted([(v,k) for k, v in counts.items()]))

#reverse sorted by value, key
print("Sorted by high to low:", sorted([(v,k) for k, v in counts.items()], reverse=True))

#identifying the person with the most commits
maxkey = max(counts, key=counts.get)
maxvalue = max(counts.values())
print(maxkey, maxvalue)