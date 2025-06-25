import random
user = input("Enter your decision --> ")
# print(user)
decision = ["rock","paper","scissors"]
ours = random.choice(decision)

user = user.lower()

def rps():
    print("computer decision --> ",ours)
    user_point = 0
    comp_point = 0
    
    if user == "rock":
        if ours == "rock":
            print("Tie!")
        elif ours == "paper":
            print("I won!")
            comp_point += 1
        elif ours == "scissors":
            print("You won!")
            user_point += 1

    elif user == "paper":
        if ours == "rock":
            print("You won!")
            user_point += 1
        elif ours == "paper":
            print("Tie!")
        elif ours == "scissors":
            print("I won!")
            comp_point += 1
            
    elif user == "scissors":
        if ours == "rock":
            print("I won!")
            comp_point += 1
        elif ours == "paper":
            print("You won!")
            user_point += 1
        elif ours == "scissors":
            print("Tie!")
    
    print("Your points --> ", user_point)
    print("My points --> ", comp_point)
            
if user in decision:
    rps()
else:
    print("You have written wrong command, pls check the spelling!")
