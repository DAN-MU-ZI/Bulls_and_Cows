import random
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

def num_generator():
    rand_num = []

    while len(rand_num) < 4:
        digit = random.randint(0, 9)
        if digit not in rand_num:
            rand_num.append(digit)
    return rand_num

def validate_input(user_input):
        if not user_input.isdigit() or len(user_input) != 4:
            print("유효하지 않은 입력입니다. 숫자 4개를 입력하세요.")
            return False
        elif len(set(user_input)) != 4:
            print("중복된 숫자가 있습니다. 다시 입력해주세요.")
            return False
        return True


def get_user_input():
    user_input = input("중복되지 않는 숫자 4개를 입력해주세요:  ")
    while not validate_input(user_input):
        user_input = input("중복되지 않는 숫자 4개를 입력해주세요:  ")

    number = int(user_input)
    return number 





# 게임을 실행하는 함수
def play_game():
    # 숫자를 뽑습니다.
    computer_num = num_generator()

    # 게임을 시작합니다.
    print("Let's play Bulls and Cows!")

    # 사용자로부터 입력을 받습니다.
    
    number = get_user_input()

    # 입력이 유효한지 확인합니다.
    
    # 숫자를 비교합니다.
    bulls, cows = compare_two_number(user_num, computer_num)
  
    # 결과를 출력합니다.

play_game()
