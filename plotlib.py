import matplotlib.pyplot as plt 
import nlp_v2 as v2

def plot(t):
 t0 = []
 t1 = v2.listing(t)
 for i in range(t):
  x = input("point") 
  t0 = t0 + [x]
 plt.plot(t1,t0)
 plt.show()
 
