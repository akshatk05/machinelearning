import random

def fit():
 while True:

  x = [1,2,3]
  y = [6]

  input1 = x[0]
  input2 = x[1]
  input3 = x[2] 

  w1 = random.randint(-10,10)
 
  w2 = random.randint(-10,10)

  w3 = random.randint(-10,10)

  w4 = random.randint(-10,10)

  i1_h = input1 + w1
  i2_h = input2 + w2
  i3_h = input3 + w3

  hnode = (i1_h + i2_h + i3_h)/3
 
  output = hnode + w4

  if output == y[0]:
   w1 = w1
   w2 = w2
   w3 = w3
   w4 = w4 
   return(w1,w2,w3,w4)
   break
  else:
   continue

def pred(a,b,c):
 input1 = a
 input2 = b
 input3 = c
 
 weights = fit()
 w1 = weights[0]
 w2 = weights[1]
 w3 = weights[2]
 w4 = weights[3]
 i1_h = input1 + w1
 i2_h = input2 + w2
 i3_h = input3 + w3

 hnode = (i1_h + i2_h + i3_h)/3

 output = hnode + w4
 
 print (output)