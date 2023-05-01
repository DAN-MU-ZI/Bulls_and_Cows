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
def print_output(bulls, cows, cnt):
    
    if bulls == 4:
        print(f"You win in {cnt} guesses!")

    else:
        print(f"{bulls} bull(s), {cows} cow(s)")
        ## 재훈님 count 함수 호출 
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
    highest_bulls = 0
    highest_cows = 0
    # 게임을 시작합니다.
    print("Let's play Bulls and Cows!")

    # 사용자로부터 입력을 받고 입력이 유효한지 확인합니다.
    
    user_num = get_user_input()
    
    # 숫자를 비교합니다.
     bulls, cows = compare_two_number(user_num, computer_num)

    # 비교한 결과 최고기록을 갱신하지 못하면 목숨을 1 감소합니다.
    #count_life
  
    # 결과를 출력합니다.
    print_output(bulls, cows)

play_game()
