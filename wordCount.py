#this is the python script I will use to parse the word choice in my writing
#
#
#@author Zach Sharpe
#@since 2017-10-6
#@modified 2017-10-6

import re
import string
from collections import Counter

fileName = input("what is the file name of the input text? ")

with open(fileName) as doc:
    count = Counter(doc.read().strip().split().lower())

print(count.most_common(100))
