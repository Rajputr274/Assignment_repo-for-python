import random
list=["rock","paper","scissor"]

# print(random.choices(list))
print("Welcome to Rock,Paper,Sciessors")
for i in range (1,4):
    
    user=input(f'select :["rock","paper","scissor"] for round {i}')
    user_count=0
    computer_count=0
    computer=random.choice(list)
    print(computer)
    if user==computer:
        print("tie")
    elif (user=="rock" and computer=="scissor") or (user=="scissor" and computer=="paper") or (user=="paper" and computer=="rock"):
        print("you win 🎊")
        user_count+=1
        print()
    else:
        print("you loose 😒")
        computer_count+=1
if user_count> computer_count:
    print(f"total score of user is {user_count} Hence you are winner 🎊🎊🎊")
else:
    print(f"score of computer is {computer_count} Hence you loose 😔😔😔😔😔😔")
    