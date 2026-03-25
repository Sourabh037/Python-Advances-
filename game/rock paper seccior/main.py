import random
'''
1 stone 
-1 paper
0 seccior
'''
computer = random.choice([-1, 0, 1])
youstr = input("enter a choice : ")
youdict = {"s" : 1, "p" : -1, "k" : 0}
reversedict = {1 : "stone", -1 : "paper", 0 : "seccior"}
you = youdict[youstr]

print(f"you = {reversedict[you]}\ncomputer = {reversedict[computer]}")

if(computer == you):
    print("draw")
else:
    if((computer - you) == -1 or (computer - you ) == 2):
        print("you win")
    else:
        print("you lose")
    # if(computer == -1 and you == 1):
    #     print("you lose")
    # elif(computer == -1 and you == 0):
    #     print("you win")
    # elif(computer == 1 and you == -1):
    #     print("you win")
    # elif(computer == 1 and you == 0):
    #     print("you lose")
    # elif(computer == 0 and you == -1):
    #     print("you lose")
    # elif(computer == 0 and you == 1):
    #     print("you win")
    # else:
    #     print("something went wrong!")
        