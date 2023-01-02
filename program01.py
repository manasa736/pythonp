def printMonthNumber(mn):
    if(mn==1):
        return "january"
    elif(mn==2):
        return "february"
    elif(mn==3):
        return "march"
    elif(mn==4):
        return "april"
    elif(mn==5):
        return "may"
    elif(mn==6):
        return "june"
    elif(mn==7):
        return "july"
    elif(mn==8):
        return "august"
    elif(mn==9):
        return "sep"
    elif(mn==10):
        return "oct"
    else:
        return "invalid"


for i in range(4):
    inpNum=int(input())
    print(printMonthNumber(inpNum))




        
