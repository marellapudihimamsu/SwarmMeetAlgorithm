import matplotlib.pyplot as p
import networkx as nx
import random as r
import math as m
x=[0]*9
y=[0]*9
for i in range(9):
  x[i]=r.randint(-100,100)
  y[i]=r.randint(-100,100)
p.plot(x,y,'bo')
p.axis([-100, 100, -100, 100])
#meet algorithm
stepsize=0.01
for dummy in range(100):
  for i in range(9):
    errx=0
    erry=0
    for j in range(9):
      errx=errx+(x[j]-x[i]) # pj-pi for x
      erry=erry+(y[j]-y[i]) # pj-pi for y
    x[i]+=stepsize*errx   
    y[i]+=stepsize*erry
    p.plot(x,y,'y.')
p.plot(x,y,'k^')  
p.title("Meet Algorithm")
p.xlabel("X axis")
p.ylabel("Y axis")

  