import numrecog2
import ai_lib
def downscale(pixels):
 new = []
 for i in pixels:
  i = (i/2)
  new.append(i)
 return(new)
data01 = "C:\_DATA\_Akku\Fun\program folder\_akshat.jpg"
data02 = numrecog2.get_pixel(data01)
data1 = downscale(data02)
target1 = 1
data11 = "C:\_DATA\_Akku\Fun\program folder\_not_akshat.jpg"
data12 = numrecog2.get_pixel(data11)
data2 = downscale(data12)
target2 = 0
pred_data21 = "C:\_DATA\_Akku\Fun\program folder\_akshat2.jpg"
pred_data22 = numrecog2.get_pixel(pred_data21)
data3 = downscale(pred_data22)
target3 = 1
def fit(training_epochs):
 best_cost = 1000
 cost = None
 params = None
 for _ in range(training_epochs):
  l0 = ai_lib.make_input_layer(data1)
  w0 = ai_lib.make_weights(64)
  b0 = ai_lib.make_biases(64)
  l1 = ai_lib.hidden_layer(l0,w0,b0,64)
  w1 = ai_lib.make_weights(64)
  b1 = ai_lib.make_biases(64)
  l2 = ai_lib.hidden_layer(l1,w1,b1,64)
  w2 = ai_lib.make_weights(64)
  b2 = ai_lib.make_biases(64)
  l3 = ai_lib.hidden_layer(l2,w2,b2,64)
  w3 = ai_lib.make_weights(64)
  b3 = ai_lib.make_biases(64)
  l4 = ai_lib.output_layer(l3,w3,w3,1)
  no = l4[0]
  cost0 = ai_lib.cost(no,target1)
  l02 = ai_lib.make_input_layer(data2)
  w02 = w0
  b02 = b0
  l12 = ai_lib.hidden_layer(l0,w0,b0,64)
  w12 = w1
  b12 = b1
  l22 = ai_lib.hidden_layer(l1,w1,b1,64)
  w22 = w2
  b22 = b2
  l32 = ai_lib.hidden_layer(l2,w2,b2,64)
  w32 = w3 
  b32 = b3
  l42 = ai_lib.output_layer(l3,w3,w3,1)
  no2 = l4[0]
  cost1 = ai_lib.cost(no2,target2)
  l12 = ai_lib.make_input_layer(data3)
  w12 = w0
  b12 = b0
  l12 = ai_lib.hidden_layer(l0,w0,b0,64)
  w12 = w1
  b12 = b1
  l12 = ai_lib.hidden_layer(l1,w1,b1,64)
  w12 = w2
  b12 = b2
  l12 = ai_lib.hidden_layer(l2,w2,b2,64)
  w12 = w3 
  b12 = b3
  l12 = ai_lib.output_layer(l3,w3,w3,1)
  no3 = l4[0]
  cost2 = ai_lib.cost(no3,target3)
  cost = cost0 + cost1 + cost2 
  if cost < best_cost:
   best_cost = cost
   params = [w0,w1,w2,w3,b0,b1,b2,b3]
  else:
   continue
 return(params)
def pred():
 pred_data0 = "C:\_DATA\_Akku\Fun\program folder\_akshat4.jpg"
 pred_data01 = numrecog2.get_pixel(pred_data0)
 pred_data = downscale(pred_data01)
 params = fit(1000)
 l0 = ai_lib.make_input_layer(pred_data)
 w0 = params[0]
 b0 = params[4]
 l1 = ai_lib.hidden_layer(l0,w0,b0,64)
 w1 = params[1]
 b1 = params[5]
 l2 = ai_lib.hidden_layer(l1,w1,b1,64)
 w2 = params[2]
 b2 = params[6]
 l3 = ai_lib.hidden_layer(l2,w2,b2,64)
 w3 = params[3]
 b3 = params[7]
 l4 = ai_lib.output_layer(l3,w3,w3,1)
 no = l4[0]
 print ('i am ')
 print (no * 100)
 print ('%')
 print ('sure this is akshat')
