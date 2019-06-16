'''import matplotlib.pyplot as suraj
a=[1,2,3,4,5,6,7,]
b=[42,24,34,50,28,17,29]
suraj.plot(a,b,color='red',linewidth=15,linestyle='dotted' )
suraj.xlabel("DAY")
suraj.ylabel("TEMPERATURE")
suraj.show()



import matplotlib.pyplot as suraj
days=[1,2,3,4,5,6,7]
max_t=[42,24,34,50,28,17,29]
suraj.plot(days,max_t,"+r--",markersize='20')
suraj.xlabel("DAY")
suraj.ylabel("TEMPERATURE")
suraj.title("weather information")
suraj.show()


import matplotlib.pyplot as suraj
days=[1,2,3,4,5,6,7]
min_t=[42,24,34,50,28,17,29]
max_t=[40,20,35,55,78,37,29]
#suraj.plot(days,min_t,"+r--",markersize='20',label=max)
#suraj.plot(days,max_t,"+r--",markersize='20',label=min)
suraj.plot(days,min_t,color="blue",label="max")
suraj.plot(days,max_t,color="orange",label="min")
suraj.plot(days,max_t)
suraj.plot(days,min_t)
suraj.xlabel("DAY")
suraj.ylabel("TEMPERATURE")
suraj.title("weather information")
suraj.legend(loc="upper left",shadow="true",fontsize="large")
suraj.grid()
suraj.savefig("weather.png")
suraj.show()'''





''' 
import matplotlib.pyplot as suraj
a=[1,2,3,4,5,6,7,]
b=[42,24,34,50,28,17,29]
suraj.plot(a,b,color='red',marker="D",markersize='10' )
suraj.xlabel("DAY")
suraj.ylabel("TEMPERATURE")
suraj.show()'''




# py chart in circular

import matplotlib.pyplot as voting
party=["bjp","bsp","sp","tmc"]
votes=[10,4,3,2]
voting.axis()
voting.pie(votes,labels=party,radius=1.5,shadow="true",explode=[0.2,0,0,0],autopct='%0.1f%%',startangle=180)
voting.show()



