import random

def cardPoint(x):       # 回傳牌數字
  if x % 13 == 0:       # 牌 A，回傳數字 11 
    return 11
  elif x % 13 >= 10:    # 牌 J、Q、K，回傳數字 10
    return 10
  else:
    return x % 13 + 1   # 牌 2~10，直接回傳牌面數字
  
def printCard( c ):     # 列印花同數字
  for i in c:
    if i // 13 == 0:     # 列印葵扇
      print('♠',end="")
    elif i // 13 == 1:   # 列印紅心
      print('♥',end="")
    elif i // 13 == 2:   # 列印方塊
      print('♦',end="")
    else:                # 列印梅花
      print('♣',end="")
    
    if i % 13 == 0:
      print('A',end=" ")
    elif i % 13 == 10:
      print('J',end=" ")
    elif i % 13 == 11:
      print('Q',end=" ")
    elif i % 13 == 12:
      print('K',end=" ")
    else:
      print(i%13+1,end=" ")
  print()

def deal(gamerCard, gamerPoint):        # 派牌給某一個
  temp = card.pop()
  gamerCard.append( temp )
  gamerPoint.append( cardPoint(temp) )

  
def printMessage():                     # 列印兩方牌與數字
  print("玩家的牌：",end=" ")
  printCard( playerCard )
  print("玩家牌面點數：",sum(playerPoint))
  #print( playerPoint )

  print("莊家的牌：",end=" ")
  printCard( bankerCard )
  print("莊家牌面點數：",sum(bankerPoint))
  #print( bankerPoint )
  print("******************************")

card = list(range(0,52))        # 洗牌
random.shuffle( card )
#print(card)

playerCard = list()
playerPoint = list()
bankerCard = list()
bankerPoint = list()

#派兩張牌給玩家
for i in range(2):
  deal(playerCard, playerPoint)
  
# 派一張牌給莊家
deal(bankerCard, bankerPoint)

printMessage()

while True:             # 玩家加牌流程
  ans = input("玩家要加牌嗎(Y/N)？")
  if ans=='N' or ans=='n':
    break
  deal(playerCard, playerPoint)
  if sum(playerPoint) > 21:
    if 11 in playerPoint:
      playerPoint[playerPoint.index( 11 )] = 1
    else:
      printMessage()
      print("玩家爆點，莊家勝利")
      break
  printMessage()

if sum(playerPoint) < 22:       # 莊家加牌流程
  while sum(bankerPoint) < 17:
    deal(bankerCard, bankerPoint)
    if sum(bankerPoint) > 21:
      if 11 in bankerPoint:
        bankerPoint[ bankerPoint.index( 11 ) ] = 1
    printMessage()  
  
  if sum(bankerPoint) > 21:
    print("莊家爆點，玩家勝利")
  elif sum(bankerPoint) > sum(playerPoint):
    print("莊家點數較大，莊家勝利")
  elif sum(bankerPoint) < sum(playerPoint):
    print("玩家點數較大，玩家勝利")
  else:
    print("和局")
