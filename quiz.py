playing = input("Do you want to play? ").lower()
user = input("Enter your name: ")

print(f'Welcome to my quiz {user}!')
if playing != 'yes':
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stands for? ").lower()
if answer == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stands for? ").lower()
if answer == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stands for? ").lower()
if answer == 'random access memory':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
print(f'{user} you got {score} questions correct! and your percentage is {(score/4)*100}%')
