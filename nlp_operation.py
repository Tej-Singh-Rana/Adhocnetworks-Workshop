# Using NLP 
import nltk
#nltk.download('all')

from urllib  import request   #  for downloading  data from url 
from  bs4  import  BeautifulSoup  #  for souping
import  time 
import  re  #  importing  regular expression 
#  Pointing to URL 
url='https://en.wikipedia.org/wiki/Machine_learning'

htmldata=request.urlopen(url)
#htmldata.read()  # it will download data in html format 
soupdata=BeautifulSoup(htmldata,'html5lib')
#      html data ,  html parser --      
#  What is  HTML parser :- is a collection of html tags that can scrape data from particular tag like h1 , html , a , p
#  now selecting a particular tag for data scrape 
atagdata=soupdata.findAll('p')
#  now converting  data into string  format  from HTML format 

mydata=""
for i in atagdata:
  mydata +=  i.text 

#print(mydata)
#  data  cleaning
web_data=mydata

# clean_data=re.sub(r'\[[0-9]*\]',' ',mydata)  #  this will remove 0 or more times number appearing in mydata
# clean_data=re.sub(r'\s+',' ',clean_data)  # it will remove one or more white spaces with single white space
# clean_data=re.sub(r'[^a-zA-Z]',' ',clean_data)  # it will remove single char from starting of the line
# clean_data=re.sub(r'\s+',' ',clean_data)  # it will remove one or more white spaces with single white space
# print(clean_data)
# print(type(clean_data))

# importing sentence tokenization

from nltk.tokenize import sent_tokenize

# passing data to sent_tokenize
sentences=sent_tokenize(web_data)
# print all sentences one by one
import time
for sent in sentences:
  print(sent)
  time.sleep(1)

  #print(sentences)

# applying word_tokenization

from nltk.tokenize import word_tokenize

list_of_word = []
for i in range(len(sentences)):
  word_tokenize(seteneces)
