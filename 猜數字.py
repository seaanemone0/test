import random
answer = random.randint(0, 100)
print(f'答案是:{answer}')

min = 0     
max = 100   

while True:
    guess = int(input(f'請猜密碼, 範圍為{min}~{max}之間的數字:'))

    
    if guess > max or guess < min:
        print('請重新輸入')

    
    elif guess == answer:
        print('恭喜答對')
        
        
        break

    
    elif guess > answer:
        print('數字太大')
        max = guess

    
    else:
        print('數字太小')
        min = guess
