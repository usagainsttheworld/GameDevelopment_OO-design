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









