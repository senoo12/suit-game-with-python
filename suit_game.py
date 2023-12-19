import random
component_list = ['rock', 'paper', 'scissors']
print("Hi, welcome to Suit Game")
print("==========================")
print(component_list)
print("You can choose theme!")
user_choices = int(input("What you'll choose? "))
if 1 <= user_choices <= 3:
    print("You choose: " + component_list[user_choices - 1])
else:
    print("Plis enter a valid number 1-3")
    exit()
    
computer_choices = random.choice(component_list)
print("Computer choose: " + computer_choices)


if component_list[user_choices - 1] == computer_choices:
    print("Draw")
elif (
    (component_list[user_choices - 1] == "rock" and computer_choices == "scissors") or
    (component_list[user_choices - 1] == "paper" and computer_choices == "rock") or
    (component_list[user_choices - 1] == "scissors" and computer_choices == "paper")
):
    print("You win!")
else:
    print("You lose!")
