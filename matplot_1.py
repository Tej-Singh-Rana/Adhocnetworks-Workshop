# if matplotlib module not installed in system then first install it.
# In jupyter !pip install matplotlib

import matplotlib.pyplot as plt
import time

# another example of data-visualization in cricket

players = ["dhoni","laxman","sachin","rohit","virat"]
scores = [200,160,300,120,230]

# now plotting 

plt.xlabel('players')
plt.ylabel('scores')
plt.bar(players,scores,label="Year 2012 score of Indian Cricket Team",color="blue")
