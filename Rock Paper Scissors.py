print("---Rock Paper Scissors---")
import random
player=int(input("1)✊,2)🖐️,3)✌️--Enter your choice: "))

one="✊ (Rock)"
Two="🖐️ (Paper)"
Three="✌️ (Scissors)"
computer=random.choice([one,Two,Three])
print(f"Computer chose: {computer}")

if player==1 and computer==one:
    print("It's a tie!")
elif player==1 and computer==Two:
    print("The computer won!")
elif player==1 and computer==Three:
    print("The player won!")
elif  player==2 and computer==one:
    print("The player won!")
elif player==2 and computer==Two:
    print("It's a tie!")
elif player==2 and computer==Three:
    print("The computer won!")
elif player==3 and computer==one:
    print("The computer won!")
elif player==3 and computer==Two:
    print("The player Won!")
elif player==3 and computer==Three:
    print("It's a tie")
else:
    print("Invalid input!")
