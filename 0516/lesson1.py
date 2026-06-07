import random


def play_guessing_game():
    """Play a simple number guessing game.

    The computer chooses a random number between 1 and 100.
    The player tries to guess the number with feedback after each guess.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("歡迎來到猜數字遊戲！")
    print("我已經想好一個 1 到 100 的整數，請開始猜吧。")

    while True:
        guess_text = input("請輸入你的猜測：")
        attempts += 1

        if not guess_text.isdigit():
            print("請輸入一個有效的整數。")
            continue

        guess = int(guess_text)

        if guess < 1 or guess > 100:
            print("請輸入 1 到 100 之間的數字。")
            continue

        if guess < secret_number:
            print("太小了，再試一次！")
        elif guess > secret_number:
            print("太大了，再試一次！")
        else:
            print(f"恭喜你，猜對了！答案是 {secret_number}。")
            print(f"你總共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    play_guessing_game()
