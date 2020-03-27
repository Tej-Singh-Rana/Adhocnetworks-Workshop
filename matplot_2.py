# if matplotlib module not installed in system then first install it.
# In jupyter !pip install matplotlib

import matplotlib.pyplot as plt
import time

# another example of data-visualization in cricket

players = ["dhoni","laxman","sachin","rohit","virat"]
scores = [200,160,300,120,230]

# now plotting 

plt.xlabel('players',fontsize=16)
plt.ylabel('scores',fontsize=16)
#'explode' must be of length 'x'
plt.pie(scores,labels=players,explode=(0.2,0,0,0,0),shadow=True,autopct='%1.f%%')#'%1.1ff%%'   # for pie chart
#plt.grid(color='red')
#plt.legend()
plt.show()
