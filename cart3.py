import gym
import random
import numpy as np
env = gym.make('CartPole-v0')
noise_scaling = 1.001
bestparams = None
parameters = np.random.rand(4)*2-1
bestreward = 0
for _ in range(1000):
 env.reset()
 newparams = parameters + (np.random.rand(4)*2-1)*noise_scaling
 reward = 0
 observation = env.reset()
 totalreward = 0
 for _ in range(200000):
  env.render()
  action = 0 if np.matmul(parameters,observation)<0 else 1
  observation , reward, done, info = env.step(action)
  totalreward = totalreward + reward
  if done:
   break
 run = totalreward
 if reward>bestreward:
  bestreward = reward
  parameters = newparams
  if reward == 200:
   break
 action = 0 if np.matmul(parameters,observation)<0 else 1
 env.step(action)

















