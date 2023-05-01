import random

def num_generator():
    rand_num = []

    while len(rand_num) < 4:
        digit = random.randint(0, 9)
        if digit not in rand_num:
            rand_num.append(digit)
    return rand_num

def count_life(cur_life, bulls, cows, highest_bulls, highest_cows):
    """
    제출한 답에서 기록 갱신을 하지 못했다면 목숨 감소
    ---------------------------------------------
    사용예시
    highest_bulls, highest_cows, cur_life = count_life(cur_life, answer, guess)
    """
    if (highest_bulls > bulls) and (highest_cows == cows) or (highest_bulls == bulls) and (highest_cows > cows):
        highest_bulls = max(highest_bulls, bulls)
        highest_cows = max(highest_cows, cows)
        return highest_bulls, highest_cows, cur_life
    else:
        return highest_bulls, highest_cows, cur_life-1

# 게임을 실행하는 함수
def play_game():
    # 숫자를 뽑습니다.
    computer_num = num_generator()

    # 게임을 시작합니다.
    print("Let's play Bulls and Cows!")

    # 사용자로부터 입력을 받습니다.

    # 입력이 유효한지 확인합니다.

    # 숫자를 비교합니다.

    # 비교한 결과 최고기록을 갱신하지 못하면 목숨을 1 감소합니다.

    # 결과를 출력합니다.

#play_game()
