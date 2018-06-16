import m
#everything is a list
def make_input_layer(nodes):
 input_layer = []
 for node in nodes:
  input_layer.append(node) 
 return(input_layer)
def make_weights(no_of_weights):
 w = []
 for _ in range(no_of_weights):
  w1 = m.get_rand(-10,10)
  w.append(w1)
 return(w)
def make_biases(no_of_biases):
 b = []
 for _ in range(no_of_biases):
  b1 = m.get_rand(-10,10)
  b.append(b1)
 return(b)
def hidden_layer(layer,w,b,number):
 a = m.matmul(layer,w)
 u = m.list_sigmoid_of(m.matadd(a,b))
 n = None
 if len(u) > number:
  n = u[:number]
 else: 
  n = u
 return(n)
def output_layer(o0,w,b,number):
 akshat = m.matmul(o0,w)
 ahaan = m.matadd(akshat,b)
 ahaanu = m.list_sigmoid_of(ahaan)
 if len(ahaanu) > number:
  ahanno = ahaanu[:number]
 else:
  ahanno = ahaanu
 return(ahanno)
def cost(pred,target):
 return((pred - target)**2)
 

 