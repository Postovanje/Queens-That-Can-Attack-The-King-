board = [["Q", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "Q", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "Q", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "K", "Q", "Q", "#", "#"],
         ["#", "#", "#", "#", "Q", "Q", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"]]

row = 0
col = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if(board[i][j] == "K"):
            row = i
            col = j

            for i in range(8):
                if(board[row][i] == "Q"):
                    print(f"[{row}, {i}]")
                    break

            for i in range(8):    
                if(board[i][col] == "Q"):
                    print(f"[{i}, {col}]")
                    break


            uzas = row
            zivi = col
            for nesto in range(8):

                if((uzas < 0) or (zivi < 0)):
                    break

                if(board[uzas][zivi] == "Q"):
                    print(f"[{uzas}, {zivi}]")
                    break
                
                uzas -= 1
                zivi -= 1

            a = row
            b = col
            for opet in range(8):

                if((a > 7) or (b > 7)):
                    break
                if(board[a][b] == "Q"):
                    print(f"[{a}, {b}]")
                    break

                a += 1
                b += 1