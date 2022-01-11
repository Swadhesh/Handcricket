import random
import time
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score1 = 0
score2 = 0
score4 = 0
score5 = 0
def second_bowling():
    score3 = 0
    print("Your final score is: ", score1)
    print("You are OUT !! Now you bowl")
    while True:
        bow2 = int(input("Enter your ball :"))
        if bow2>10:
            print("Your ball should be within 10")
            continue
        rand = random.choice(list)
        bat2 = print("Computer's shot :", rand)
        if (bow2 == rand):
            if (score1 > score3):
                print("You won")
                break
            elif (score1 == score3):
                print("Match Draw")
                break
            else:
                print("You Lost")
                break
        else:
            global score2
            score2 += rand
            score3 = score2
            print("Computer's score is :", score2)
            if (score3 > score1):
                print("You lost")
                break
def first_batting():
    while True:
        bat1 = int(input("Enter your shot :"))
        rand = random.choice(list)
        bow1 = print("Computer's ball :", rand)
        if bat1>10:
            print("Your shot should be within 10")
            continue
        if (bat1 == rand):
            second_bowling()
            break
        else:
            global score1
            score1 += bat1
            print("Your score is :", score1)
def second_batting():
    score3 = 0
    print("Computer's final score is :", score4)
    print("Computer is OUT !! Now you Bat")
    while True:
        bat4 = int(input("Enter your shot :"))
        if bat4>10:
            print("Your shot should be within 10")
            continue
        rand = random.choice(list)
        bow4 = print("Computer's ball :", rand)
        if (bat4 == rand):
            if (bat4 > score4):
                print("You Won")
                break
            elif (bat4 == score4):
                print("Match Draw")
                break
            else:
                print("You lost")
                break
        else:
            global score5
            score5 += bat4
            score3 = score5
            print("Your score is :", score5)
            if (score3 > score4):
                print("You WON")
                break
def first_bowling():
    while True:
        bow3 = int(input("Enter your ball :"))
        if bow3>10:
            print("Your ball should be within 10")
            continue
        rand = random.choice(list)
        bat3 = print("Computer's shot :", rand)
        if (bow3 == rand):
            second_batting()
            break
        else:
            global score4
            score4 += rand
            print("Computer score is :", score4)
print("WELCOME TO THE TOSS !!")
print()
choi = input("Choose between head(h)/tails(t): ")
choice = choi.lower()
list1 = ["h", "t"]
option = ["bat", "bowl"]
randa = random.choice(list1)
print(choi," is the call and it is.....!")
time.sleep(2)
print(randa)
if randa == choice:
    opinion = int(input("You WON the toss! Choose if you want to bat(1) or bowl(2): "))
    if (opinion == 1):
        first_batting()
    elif (opinion == 2):
        first_bowling()
    else:
        print("Choose any one of specified two options")
else:
    randa2 = random.choice(option)
    print("Computer won the toss and chooses to:", randa2)
    if randa2 == "bat":
        first_bowling()
    else:
        first_batting()