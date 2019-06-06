# -*- coding: utf-8 -*-
#Hyeon Jeong Byeon

import time

board = [' '] * 9

###---functions---###

def drawBoard():
    print(" %c | %c | %c "%(board[0],board[1],board[2]))
    print("___|___|___")
    print(" %c | %c | %c "%(board[3],board[4],board[5]))
    print("___|___|___")
    print(" %c | %c | %c "%(board[6],board[7],board[8]))
    print("   |   |   ")

def checkWin():
    #수평선상으로 같은 마크가 있는지 검사
    if (board[0] == board[1] and board[1] == board[2] and board[0] != ' '):
        return 1
    elif (board[3] == board[4] and board[4] == board[5] and board[3] != ' '):
        return 1
    elif (board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
        return 1
    #수직선상에 같은 마크가 있는지 검사
    elif (board[0] == board[3] and board[3] == board[6] and board[0] != ' '):
        return 1
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        return 1
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return 1
    #대각선상으로 이겼는지 검사
    elif (board[0] == board[4] and board[4] == board[8] and board[4] != ' '):
        return 1
    elif (board[2] == board[4] and board[4] == board[6] and board[4] != ' '):
        return 1
    #위의 경우가 아니면서 빈 셀이 아닌 경우 검사, 즉 비긴 경우
    elif (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' '
          and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
        return 2
    #위의 조건에 맞지 않으면 아직 빈 셀이 있는 경우임
    else:
        return 0
    
        
###---Main Screen---###

print("Tic-Tac-Toe 게임 시작 (개발자 : 변현정)")
print("선수 1 [X] --- 선수2 [O]\n")
print("")
print("")
print("준비중입니다...")
time.sleep(1)

drawBoard()

gameCount = 1
win = 0
while True:
    if gameCount % 2 == 1:
        print("선수1 차례입니다.")
        mark = "X"
    else:
        print("선수2 차례입니다.")
        mark = "O"
    position = int(input("마크하기를 원하는 위치(1-9)를 선택하세요:"))
    idx = position - 1
    board[idx] = mark
    drawBoard()
    win = checkWin()
    if win == 2:
        print("무승부")
        break
    elif win == 1 and gameCount % 2 == 1:
        print("선수1 승리!")
        break
    elif win == 1 and gameCount % 2 == 0:
        print("선수2 승리!")
        break
    gameCount += 1
