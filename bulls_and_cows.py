import random

def num_generator():
    rand_num = []

    while len(rand_num) < 4:
        digit = random.randint(0, 9)
        if digit not in rand_num:
            rand_num.append(digit)
    return rand_num

# 게임을 실행하는 함수
def play_game():
    # 숫자를 뽑습니다.
    computer_num = num_generator()


    # 게임을 시작합니다.
    print("Let's play Bulls and Cows!")

    # 사용자로부터 입력을 받습니다.

    # 입력이 유효한지 확인합니다.

    # 숫자를 비교합니다.

    # 결과를 출력합니다.

#play_game()
