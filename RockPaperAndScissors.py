"""
Rock : Paper (Paper)
Paper : Scissors (Scissors)
Rock : Scissors (Rock)
"""

import random


def inputHandler(inpt):
    inpt=inpt.lower()
    passOutput="rock paper scissors"
    r,p,s=passOutput.split()
    rval,pval,sval=0,0,0
    inptList=list(inpt)
    pList=[list(r),list(p),list(s)]
    for k in pList:
        i=0
        for l in k:
            try:
                if(l == inptList[i]):
                    if(k == list(r)):
                        rval+=1
                    elif(k == list(p)):
                        pval+=1
                    elif(k == list(s)):
                        sval+=1
                i+=1
            except IndexError:
                break
    if(rval == pval and pval == sval):
        print("Invalid input")
        return 0
    else:
        w=max(rval,pval,sval)
        if(w== rval):
            return r
        elif(w== pval):
            return p
        elif(w== sval):
            return s
        
            
    
# computer's choice
def computers_choice():
    return (random.choice([-1,0,1]))

def win_dec(user,computer):
    if (user == computer):
        print("It's a tie")
    else:
        if ((user == 0 and computer == -1) or (user == 1 and computer == 0) or  (user == -1 and computer == 1)):
            print("User Wins !")
        else:
            print("Computer Wins!")





rps ={"rock":-1,"paper":0,"scissors":1}
revRPS={-1:"rock",0:"paper",1:"scissors"}
user = ""

while(True):
    print("Enter '0' to exit")

    uinput = input("Your choice: ")
    if ((uinput) == "0" or (user) == 0):
        break
    user = inputHandler(uinput)
    computer = computers_choice()
    print(f"Computer's choice: {revRPS[computer]}")
    try:
        win_dec(rps[user],computer)
    except KeyError:
        break


    
    