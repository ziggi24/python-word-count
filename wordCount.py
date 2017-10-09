#this is the python script I will use to parse the word choice in my writing
#
#
#@author Zach Sharpe
#@since 2017-10-6
#@modified 2017-10-6

#for this project we will use the Counter Object, which is based on the python
#dictionaries. this will automatically handle the parsing of words, as well as
#counting their frequency. It will also provide the most_common() method that
#we use to calculate the 100 most common and return them to the user. The
# documentation for Counter objects can be found here:
#
#https://docs.python.org/3/library/collections.html
from collections import Counter

# here we ask the user which file to parse. For the sake of this example the
#file will always be the included input.txt, however I added this input so that
#other people could take this code and use it without having to modify it.
fileName = input("what is the file name of the input text? ")

# with the file name given, we will open the file, and read it.
#This is the main loop of the script. This check to see if the file exists, then
#opens it, and proceeds to loop through every word and adds it to the Counter
#object, called count here. This will return completed when there are no more
#words to parse.
with open(fileName) as doc:
    count = Counter(doc.read().strip().split())

#in this look we format the print. We loop through every value in the top 100
#most common, and then print them out on their own line. 
for key, value in count.most_common(100):
	print(key+ " - " + str(value))
