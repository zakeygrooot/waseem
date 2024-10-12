import random
print("Welcome to Waseem's rock, paper, scissors game.")
user_name = input("Before we start, what's your name?")
if user_name == "sapna" or user_name == "Sapna":
    print(f"Hello {user_name} my love. Shall we start?")
else:
    print(f"Hello {user_name}. My name is Waseem.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer_choose = random.randint(0,2)
question = int(input(f"So {user_name}. What do you choose? 0 for Rock, 1 "
                 "for Paper or 2 for Scissors. \n"))
images = [rock, paper, scissors]
numbers_0_1_2 = [0,1,2]
# Rock wins against scissors. 0 win over 2
# Paper wins against rock. 1 win over 0
# Scissors win against paper. 2 win over 1
if question == computer_choose:
    print(f"Computer chose: {computer_choose}")
    print("Draw")
elif question == 0 and computer_choose == 2:
    print(f"You chose: Rock\n{rock}")
    print(f"Computer chose: Scissors\n{scissors}")
    print("You won!")
elif question == 1 and computer_choose == 0:
    print(f"You chose: Paper\n{paper}")
    print(f"Computer chose: Rock\n{rock}")
    print("You won!")
elif question == 2 and computer_choose == 1:
    print(f"You chose: Scissors\n{scissors}")
    print(f"Computer chose: Paper\n{paper}")
    print("You won!")
elif computer_choose == 0 and question == 2:
    print(f"You chose: Scissors\n{scissors}")
    print(f"Computer chose: Rock \n{rock}")
    print("You lost!")
elif computer_choose == 1 and question == 0:
    print(f"You chose: Rock\n{rock}")
    print(f"Computer chose: Paper\n{paper}")
    print("You lost!")
elif computer_choose == 2 and question == 1:
    print(f"You chose: Paper\n{paper}")
    print(f"Computer chose: Scissors\n{scissors}")
    print("You lost!")
else:
    print(f"Your choice was out of rule")
    print(f"Computer chose:\n{computer_choose}")
    print("You lost.")
# Rock wins against scissors. 0 win over 2
# Paper wins against rock. 1 win over 0
# Scissors win against paper. 2 win over 1