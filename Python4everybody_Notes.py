#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt

#!!!to delete right space/new lines  
#!!!to upper case
#fname = raw_input('Enter the file name:')
#mydata = open(fname)
#for line in mydata:
	#line = line.rstrip()
	#print line.upper()

#7.2 
#count lines starts with 'X-DSPAM-Confidence:' and extract the number following it
#!!!convert charactor to float point
#!!!creat new variable for new line and add to the old variabel (sum of the old lines)
fname = raw_input('Enter the file name:')
mydata = open(fname)
counter = 0
mynum =0
for line in mydata:
	if line.startswith('X-DSPAM-Confidence:'): 
		#print line
		counter = counter + 1
		#print counter
		bf = line.find(':')
		#print bf
		newnum = line[bf+2:]
		mynum = float(mynum) + float(newnum)
		#print mynum
#print counter
#print mynum	
ave = mynum / counter
print "Average spam confidence: ", ave 	

#8.4
#read romeo.txt. for each line, split line into list. for each word on each line
#check to see if the word is already in the list and if not append to the list. 
#when program completes, sort and print the resulting words.
fname = raw_input('Enter file name:')
mydata = open (fname)
unique_words = list()
for line in mydata:
	splitLine = line.split()
	for word in splitLine:
		if word not in unique_words:
			unique_words.append(word)
unique_words.sort()			
print unique_words

#8.5
# read mbox-short.txt by line. for lines starts with "From". split the line 
# and print out the second word. Then print out a count at the end.
fname = raw_input('Enter file name:')
mydata = open (fname)
counter = 0
for line in mydata:
	line = line.rstrip()
	if not line.startswith('From '): continue
	counter = counter + 1
	words = line.split()
	print words[1]
print "There were", counter, "lines in the file with From as the first word"

#9.4 read from mbox-short.txt and figure who has sent the greatest number
# of mail messages (looks for "From" lines and takes the second word of those lines)
fname = raw_input('Enter file name:')
mydata = open (fname)

emails = list()
for line in mydata:
        line = line.rstrip()
	if not line.startswith('From '): continue
	words = line.split()
	emails.append(words[1])
#print emails         

countEmail = dict()
for email in emails:
	countEmail[email] = countEmail.get(email,0) + 1
#print countEmail	

bigcount = None        
big_email_sender = None
for email,count in countEmail.items():
	if bigcount is None or count > bigcount:
		big_email_sender = email
		bigcount = count
print big_email_sender, bigcount	











