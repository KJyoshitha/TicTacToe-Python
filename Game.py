from tkinter import *

root = Tk()


def intro():
    print("\n\n\t\t\tTIC - TAC - TOE\n")
    print("GAMEBOARD POSITIONS:")
    print('\t' '\t    ' + '1' + '\t  |' + '      ' + '2' + '      |' + '     ' + '3')
    print('\t--------------+-------------+------------')
    print('\t' '\t    ' + '4' + '\t  |' + '      ' + '5' + '      |' + '     ' + '6')
    print('\t--------------+-------------+------------')
    print('\t' '\t    ' + '7' + '\t  |' + '      ' + '8' + '      |' + '     ' + '9')
    print("Get your symbol in a line horizontally, vertically or diagonally to win.")
    print("****************************************************************************\n")


def main():
    intro()

    theBoard = {'1': ' ', '2': ' ', '3': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '7': ' ', '8': ' ', '9': ' '}

    board_keys = []

    for key in theBoard:
        board_keys.append(key)

    def printBoard(board):
        print('\t' '\t    ' + board['1'] + '\t |' + '      ' + board['2'] + '      |' + '     ' + board['3'])
        print('\t-------------+-------------+------------')
        print('\t' '\t    ' + board['4'] + '\t |' + '      ' + board['5'] + '      |' + '     ' + board['6'])
        print('\t-------------+-------------+------------')
        print('\t' '\t    ' + board['7'] + '\t |' + '      ' + board['8'] + '      |' + '     ' + board['9'])

    # Main function
    def game(winX, winO, player1, player2):
        turn = 'X'
        count = 0
        for i in range(10):
            printBoard(theBoard)
            if i != 9:
                move = input(turn + "'s turn: ")
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Checking if player X or player O has won.
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['7'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['4'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['1'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['4'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['5'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['6'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['3'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\nGAME OVER.\n")
                    if (theBoard['9'] == 'X'):
                        winX += 1
                    else:
                        winO += 1
                    print("----- ", turn, "WON! -----")
                    break

            # Full board with no wins->tie
            if count == 9:
                print("\nGAME OVER.\n")
                print("---- It's a TIE!! ----")

            # Change player after every move.
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

        print(player1, ":", winX)
        print(player2, ":", winO)

        # Restart the game or not.
        restart = input("Do want to play Again?(y/n): ")
        if restart.lower() == 'y':
            for key in board_keys:
                theBoard[key] = " "
            game(winX, winO, player1, player2)
        elif restart.lower() == 'n':
            import mysql.connector as sql
            mydb = sql.connect(host="localhost", user="root", password="1234", database="tictactoe")
            mycursor = mydb.cursor()
            b = "insert into playerdata values(' " + player1 + " ',' " + c1 + " ',' " + str(winX) + " ')"
            mycursor.execute(b)
            c = "insert into playerdata values(' " + player2 + " ',' " + c2 + " ',' " + str(winO) + " ')"
            mycursor.execute(c)
            mydb.commit()
            print("Succesfully entered values to table.")
            print("-------------------------------------------------------")
        else:
            print("Wrong choice.")

    winX = 0
    winO = 0
    c1 = "X"
    c2 = "O"

    # Player's names
    player1 = input("Name of Player 1: ")
    player2 = input("Name of Player 2: ")
    print("THE CHARACTER OF PLAYER 1 IS X AND PLAYER 2 IS O")
    game(winX, winO, player1, player2)


# Leaderboard
def leaderboard():
    import mysql.connector as sql
    mydb = sql.connect(host="localhost", user="root", password="1234", database="tictactoe")
    mycursor = mydb.cursor()
    cmd = "select * from playerdata order by Wins desc"

    mycursor.execute(cmd)
    result = mycursor.fetchall()
    print('[Name,Symbol,Wins]')
    for a in result:
        print(a)
    print("-----------------------------------------------------------------")


# Exit game
def exitt():
    while True:
        print("\nGame Closed.")
        root.destroy()
        break


# -------------------------------------------------------------------------------------
# mysql connection
import mysql.connector as mysql

mydb = mysql.connect(host='localhost', user='root', passwd='1234')
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS tictactoe")
mydb.commit()
mydb.close()

mydb2 = mysql.connect(host='localhost', user='root', passwd='1234', database='tictactoe')
mycursor2 = mydb2.cursor()
mycursor2.execute("CREATE TABLE if not exists playerdata(Name VARCHAR(20) NOT NULL, Symbol VARCHAR(2) NOT NULL, Wins INT NOT NULL)")
mydb2.commit()
mydb2.close()

# Creating tkinter master window
root.maxsize(600, 400)
root.minsize(600, 400)
root.title("TICTACTOE")
root.configure(bg='black')

line = Label(root, bg="black", fg="white", text=" TIC-TAC-TOE ", font="Stencil 35 bold")
line.pack(pady=60)

# Play button
b1 = Button(root, bg="black", fg="white", text="PLAY", font="Rockwell 15 bold", command=main)
b1.pack(side="top", padx=10, pady=10)

# Leaderboard button
b2 = Button(root, bg="black", fg="white", text="LEADERBOARD", font="Rockwell 15 bold", command=leaderboard)
b2.pack(side="top", pady=10, padx=10)

# Exit button
b3 = Button(root, bg="black", fg="white", text="EXIT", font="Rockwell 15 bold", command=exitt)
b3.pack(side="top", pady=10, padx=10)

root.mainloop()
