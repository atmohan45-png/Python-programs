import random   
class game:
    def guess():
        user=input("Enter your choice (rock, paper, scissors): ")
        choices=["rock","paper","scissors"]
        computer=random.choice(choices)
        print("computer choice is: ",computer)
        if user==computer:
            print("Its a tie")
            game.guess()
        elif(user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
            print("You win!")
        else:
            print("Computer wins!") 
game.guess()  
        