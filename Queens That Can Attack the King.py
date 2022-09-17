board = [["Q", "Q", "Q", "#", "#", "#", "#", "#"],
         ["Q", "K", "Q", "#", "#", "#", "#", "#"],
         ["Q", "Q", "Q", "Q", "#", "#", "#", "#"],
         ["#", "#", "Q", "#", "Q", "Q", "#", "#"],
         ["#", "#", "#", "Q", "#", "Q", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "Q"]]


def main() -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == "K"):
                kRow = i
                kCol = j
                
                print(f"King [{kRow}, {kCol}]")
                
                for up in range(8):
                    if(board[up][kCol] == "Q"):
                        print(f"[{up}, {kCol}]")
                        if(board[kRow][up] == "Q"):
                            print(f"[{kRow}, {up}]")
                
                leftPD, leftND = kRow, kRow
                rightPD, rightND = kCol, kCol

                pr, nr = True, True
                pl, nl = True, True

                for dg in range(8):
                    if(leftPD < 7): leftPD += 1
                    if(rightPD < 7): rightPD += 1

                    if(leftND > 0): leftND -= 1
                    if(rightND > 0): rightND -= 1
                    
                    if(board[leftND][rightND] == "Q" and nr == True):
                        print(f"[{leftND}, {rightND}]")
                        nr = False

                    if(board[leftPD][rightPD] == "Q" and pr == True):
                        pr = False                   
                        print(f"[{leftPD}, {rightPD}]")

                    if(board[leftPD][rightND] == "Q" and pl == True):
                        pl = False
                        print(f"[{leftPD}, {rightND}]")

                    if(board[leftND][rightPD] == "Q" and nl == True):
                        nl = False
                        print(f"[{leftND}, {rightPD}]")

                    if((pr == False) and (nr == False) and (pl == False) and (nl == False)):
                        break


if __name__ == "__main__":
    main()
