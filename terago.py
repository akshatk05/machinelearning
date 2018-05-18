import sgfmill
import sgfmill.boards
import sgfmill.ascii_boards
import sgfmill.common
import random
import sgfmill.sgf
import random
import numpy as np
import sklearn
from sklearn import tree
from sklearn.linear_model import LinearRegression
wscore = 0
bscore = 0
l1 = [0,1,2,3,4,5,6,7,8]
l2 = [0,1,2,3,4,5,6,7,8]
l10 = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6],[5,7],[5,8],[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[6,8],[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7],[8,8]]
p1score = 0
p2score = 0
board = sgfmill.boards.Board(9)
Board = sgfmill.boards.Board(9)
def move1():
 print (sgfmill.ascii_boards.render_board(board))
 x = input("give your move [eg. a4] ") 
 y = sgfmill.common.move_from_vertex(x, 9) 
 y = list(y)
 a = y[0]
 c = y[1]
 board.play(a, c, 'b')
 Board.play(a, c, 'b')
 print (sgfmill.ascii_boards.render_board(board))
def move2():
 print (sgfmill.ascii_boards.render_board(board))
 x = input("give your move [eg. a4] ")
 y = sgfmill.common.move_from_vertex(x, 13) 
 y = list(y)
 a = y[0]
 c = y[1]
 board.play(a, c, 'w')
 print (sgfmill.ascii_boards.render_board(board))
def eval(board):
 wscore = 0
 bscore = 0
 for i in l10:
  fk = i[0]
  jk = i[1]
  ad = board.get(fk,jk)
  if ad == 'w':
   wscore = wscore + 1
  elif ad == 'b':
   bscore = bscore + 1
  elif ad != 'w' and ad != 'b':
   wscore = wscore
   bscore = bscore
 aw = ((wscore - bscore)/(100)) * (100 - bscore)
 return(aw)
def ai_move():
  for i in l10:
   gt = i[0]
   gy = i[1]
   gg = Board.get(gt,gy)
   if gg == 'w' or gg == 'b':
    continue
   else:
    ba = eval(Board)
    Board.play(gt,gy,'w')
    ab = eval(Board)
    fg = ab - ba
    if fg > 1:
      gt = i[0]
      gy = i[1]
      board.play(gt,gy,'w')
      print (sgfmill.ascii_boards.render_board(board))
      break
    else:
     continue
     #undo Board move
     #make an ai predict moves with an everchanging data set(data+current move),(data + current move and also do monte carlo search and then evaluate weather ai or monte carlo search was better
def ai_play(t):
 for i in range(t):
  for i in range(100):
   e = random.choice(l1)
   e = int(e)
   f = random.choice(l2)
   f = int(f) 
   gg = board.get(e,f)
   if gg == 'w' or gg == 'b':
    continue
   else:
    board.play(e,f,'w')
    break
  for i in range(100):
   e = random.choice(l1)
   e = int(e)
   f = random.choice(l2)
   f = int(f) 
   gg = board.get(e,f)
   if gg == 'w' or gg == 'b':
    continue
   else:
    board.play(e,f,'b')
    break
  print (sgfmill.ascii_boards.render_board(board))
  wscore = 0
  bscore = 0
 for i in l10:
  fk = i[0]
  jk = i[1]
  ad = Board.get(fk,jk)
  if ad == 'w':
   wscore = wscore + 1
  elif ad == 'b':
   bscore = bscore + 1
  elif ad != 'w' and ad != 'b':
   wscore = wscore
   bscore = bscore
 aw = wscore - bscore
 return(aw)
def ai_move():
  for i in l10:
   gt = i[0]
   gy = i[1]
   gg = Board.get(gt,gy)
   if gg == 'w' or gg == 'b':
    continue
   else:
    ba = eval(Board)
    Board.play(gt,gy,'w')
    ab = eval(Board)
    fg = ab - ba
    if fg > 1:
      gt = i[0]
      gy = i[1]
      board.play(gt,gy,'w')
      print (sgfmill.ascii_boards.render_board(board))
      break
    else:
     continue

lr = 0.001
input_size = 64
def smart():
 board1 = sgfmill.boards.Board(9)
 while True:
  xau = []  
  yau = []
  print (sgfmill.ascii_boards.render_board(board1))
  x = input("give your move [eg. a4] ") 
  y = sgfmill.common.move_from_vertex(x, 9) 
  y = list(y)
  ak = y[0]
  ah = y[1]
  board1.play(ak, ah,'b' )
  print (sgfmill.ascii_boards.render_board(board1)) 
  clf = tree.DecisionTreeClassifier()
  for i  in range(1000):
   for i in range(100):
    e = random.choice(l1)
    e = int(e)
    f = random.choice(l2)
    f = int(f) 
    gg = board.get(e,f)
    if gg == 'w' or gg == 'b':
     continue
    else:
     fi = eval(board)
     board.play(e,f,'w')
     c = eval(board)
     big = fi-c 
     if big > 2:
      a = [e,f]
      xau = xau + [a]
      break 
     else:
      continue
   for i in range(100):
    e = random.choice(l1)
    e = int(e)
    f = random.choice(l2)
    f = int(f) 
    gg = board.get(e,f)
    if gg == 'w' or gg == 'b':
     continue
    else:
     fi = eval(board)
     board.play(e,f,'w')
     c = eval(board)
     big = f-c 
     if big > 2:
      b = [e,f]
      yau = yau + [b]
      break
  trying = len(yau)
  flying = len(xau)
  if flying > trying:
   xau = xau[:trying]
  if trying > flying:
   yau = yau[:flying]
  clf.fit(xau,yau)
  move_list = [[ak, ah]]
  pred =  clf.predict(move_list)
  p = pred[0][0]
  p = p.astype(int)
  r = pred[0][1]
  r = r.astype(int)
  tyt = board1.get(p,r)
  if tyt == 'w' or tyt == 'b':
   for i in range(100):
    eee = random.choice(l1)
    eee = int(eee)
    fff = random.choice(l2)
    fff = int(fff) 
    ggg = board1.get(eee,fff)
    print (ggg)
    if ggg == 'w' or ggg == 'b':
     continue
    else:
     b = [eee,fff]
     board1.play(eee,fff,'w')
     break    
  else:
   board1.play(p,r,'w')