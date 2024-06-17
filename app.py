# 使用 python app.py 命令在主控台上執行小遊戲。
# 在命令提示字元，輸入其中一個遊戲選項：rock、paper 或 scissors。
# 小遊戲應該通知玩家，玩家贏了、輸了或與對手打平。
# 選擇繼續玩遊戲。
# 在命令提示字元，輸入 screen。
# 如果玩家輸入的選項無效，小遊戲應該會通知玩家。
# 重複步驟 2 和 4 可玩幾個回合，並選擇不繼續玩。
# 檢查小遊戲是否已終止及是否顯示您的分數，通知您獲勝次數和回合數。
# 根據上述要求，編寫一個 Python 程式。
def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to play.")
    print("Enter 'screen' to display the score.")
    print("Enter 'quit' to end the game.")
    print("")

    wins = 0
    rounds = 0

    while True:
        player = input("Enter your choice: ").lower()
        if player == "quit":
            break
        elif player == "screen":
            print("Wins:", wins)
            print("Rounds:", rounds)
            print("")
            continue
        elif player != "rock" and player != "paper" and player != "scissors":
            print("Invalid choice. Please try again.")
            print("")
            continue

        import random
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)

        print("Computer chose:", computer)

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
            wins += 1
        elif player == "paper" and computer == "rock":
            print("You win!")
            wins += 1
        elif player == "scissors" and computer == "paper":
            print("You win!")
            wins += 1
        else:
            print("You lose!")

        rounds += 1
        print("")

    print("Thanks for playing!")
    print("Wins:", wins)
    print("Rounds:", rounds)

if __name__ == "__main__":
    main()



