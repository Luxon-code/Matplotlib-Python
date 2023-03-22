import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y,ls="-.")

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Promedio del peso y altura", loc= "left",fontdict=font1)
plt.xlabel("Peso", fontdict=font2)
plt.ylabel("Altura",fontdict=font2)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()