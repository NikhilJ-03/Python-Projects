import random
Ans=input("Would you like to play a game called Stone Paper Scissors (Yes/No): ")
if Ans=="Yes":
    Name=input("Your Name?: ")
    age=int(input('Age?: '))
    print("To start first you have to give a try to your luck.")
    print("Computer will generate a random number from 1-100.")
    print("If number come out to be even you can continue otherwise you can not.")
    begin=str(input("Type Begin to continue: "))
    if begin=="Begin":
        randnum=random.randint(1,100)
        print(f"Random number by computer is {randnum}.")
        if randnum%2==0:
            print("Congrats number came out to be even.")
            computer=random.choice([-1,0,1])
            response=input("Enter your response: ")
            youdict={1:"Stone",-1:"Scissors",0:"Paper"}
            revdict={"S":1,"C":-1,"P":0}
            younum=revdict[response]
            print(f"You Choose {youdict[younum]}\nComputer Choose {youdict[computer]}")
            if computer==younum:
                print("It's a draw.")
            else:
                if computer==1 and  younum==0:
                    print("You Win!")
                elif computer==1 and younum==-1:
                    print("You Lose!")
                elif computer==-1 and younum==1:
                    print("You Win!")
                elif computer==-1 and younum==0:
                    print("You Lose!")
                elif computer==0 and younum==1:
                    print("You Lose!")
                elif computer==0 and younum==-1:
                    print("You Win!")
        else:
            print("Oops! you are out of luck. Thank you!")
    else:
        print("Okay")
else:
    print("Thank You!")