def compare_two_number(user_num, computer_num):
    bulls = 0
    cows = 0

    user_num = str(user_num)
    computer_num = str(computer_num)
    
    for i in range(4):
        if (user_num[i] == computer_num[i]):
            bulls += 1
        elif (user_num[i] in c):
            cows += 1
    
    return bulls, cows


# 게임을 실행하는 함수
def play_game():
    # 숫자를 뽑습니다.

    # 게임을 시작합니다.
    print("Let's play Bulls and Cows!")

    # 사용자로부터 입력을 받습니다.

    # 입력이 유효한지 확인합니다.
    
    # 숫자를 비교합니다.
    bulls, cows = compare_two_number(user_num, computer_num)
  
    # 결과를 출력합니다.

play_game()
