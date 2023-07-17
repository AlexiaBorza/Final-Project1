from visuals import draw
choices = ["rock", "paper", "scissors"]

a_choice = input("Choose rock, paper or scissors: '1' for 'rock', '2' for 'paper', '3' for 'scissors'. ").lower()
b_choice = input("Choose rock, paper or scissors: '1' for 'rock', '2' for 'paper', '3' for 'scissors'. ").lower()

if a_choice == '1':
    a_choice = "rock"
elif a_choice == '2':
    a_choice = "paper"
else:
    a_choice = "scissors"
print("\nPlayer a chose", a_choice + draw(a_choice))

if b_choice == '1':
    b_choice = "rock"
elif b_choice == '2':
    b_choice = "paper"
else:
    b_choice = "scissors"
print("\nPlayer b chose", b_choice + draw(b_choice))

if a_choice == b_choice:
    print('It is a tie!\n')
elif (a_choice == "rock" and b_choice == "scissors") or (a_choice == "paper" and b_choice == "Rock") \
        or (a_choice == "scissors" and b_choice == "paper"):
    print("Player a won!\n")
else:
    print("\nPlayer b won!\n")

print("Thanks for playing!")
