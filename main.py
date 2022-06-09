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

#Write your code below this line 👇
import random
lis_rps = [rock, paper, scissors]
random_lis = random.choice(lis_rps)
players_in = int(input("what do you choose? type 0 for rock, 1 for paper, or 2 for scissors\n"))
if players_in == 0:
  print(rock)
  print(random_lis)
elif players_in == 1:
    print(paper)
    print(random_lis)
elif players_in == 2:
    print(scissors)
    print(random_lis)
if players_in == 0 and random_lis == rock:
  print("woohoo!!.. you WON the game")
elif players_in == 1 and random_lis == paper:
  print("woohoo!!.. you WON the game")
elif players_in == 2 and random_lis == scissors:
  print("woohoo!!.. you WON the game")
else:
  print("BAD LUCK!!.. Please Proceed Next time..")