def  USER_INPUT():
    length=-1
    length=input("ENTER THE DESIRED LENGTH OF PASSWORD")
    if length<=0 :
        print("ERROR INVALID PASSWORD LENGTH")
    diffi_level=-1
    diffi_level=input("ENTER THE DESIRED DIFFICULTY OF THE PASSWORD \nLEVEL'1'\nLEVEL'2'\nLEVEL'3'\n<--->\n")
    if (diffi_level!=1 and diffi_level!=2 and diffi_level!=3):
        print("ERROR WRONG DIFFICULTY LEVEL")
        
    return length,diffi_level

USER_INPUT()
