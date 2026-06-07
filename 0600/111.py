import random

def play_guessing_game():
    """Play a simple number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("歡迎來到猜數字遊戲！")
    print("我已經想好一個 1 到 100 的整數，請開始猜吧。")

    while True:
        guess_text = input("請輸入 1 到 100 的整數：").strip()
        if not guess_text.isdigit():
            print("請輸入一個有效的整數。")
            continue

        guess = int(guess_text)
        if guess < 1 or guess > 100:
            print("請輸入 1 到 100 之間的數字。")
            continue

        attempts += 1
        if guess < secret_number:
            print("太小了，請再試一次。")
        elif guess > secret_number:
            print("太大了，請再試一次。")
        else:
            print(f"恭喜你猜對了！答案是 {secret_number}。")
            print(f"你總共猜了 {attempts} 次。")
            break


def main():
    while True:
        play_guessing_game()
        again = input("要再玩一次嗎？(y/n)：").strip().lower()
        if again not in ("y", "yes"):
            print("謝謝遊玩，再見！")
            break


if __name__ == "__main__":
    main()
