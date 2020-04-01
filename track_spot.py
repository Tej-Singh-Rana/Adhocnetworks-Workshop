import geocoder    # importing geocoder module

print("Enter your ip address : ")
ip_addr = (input())
g = geocoder.ip(ip_addr)         # entering ip address of mine
print("Your city name is : ",g.city,"\nYour state name is : ",g.state)

#!pip install google
# To get the information around the city for corona-virus.
from googlesearch import search
my_results_list = []
for i in search('Coronavirus'+ g.city,tld='com',lang='en',num=1,start=0,stop=5,pause=2.0):
  my_results_list.append(i)
  print(i)
