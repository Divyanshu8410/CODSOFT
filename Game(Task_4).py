import random
def Game():
    print("----Welcome to Rock Paper Scissors Game----")
    print("Choice: Rock Paper Scissors")
    User_Choice=input("Enter the choice : ").lower()
    options=['rock','paper','scissors']
    if User_Choice not in options:
        print("Invalid choice! Please choose Rock, Paper or Scissors.")
        return
    Mix = random.choice(options)
    print("Computer Choice : ",Mix)
    if Mix==User_Choice:
        print("Game is Tie!")
    elif (User_Choice == 'rock' and Mix == 'scissors') or \
         (User_Choice == 'paper' and Mix == 'rock') or \
         (User_Choice == 'scissors' and Mix == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    Game()
    again=input("You want to play this game again (yes or no) : ").lower()
    if again != "yes":
        print("Thank You For Playing Game!")
        break



