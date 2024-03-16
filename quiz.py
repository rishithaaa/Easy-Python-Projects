print("Welcome to my computer quiz!")

playing = input("do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
    
print("okay! let's play:)")
score = 0

answer = input("What does CPU stand for: ")
if answer.lower() == "central processing unit":
    print("Correct!") 
    score += 1
else:
    print("Incorrect!")
    
answer = input("Name an input device that has keys: ")
if answer.lower() == "keyboard":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("name  a type of output device with speakers: ")
if answer.lower() == "speaker":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("name  the programming language used in this game: ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " +str(score)+ " questions correct!")
print("you got " +str((score/4) * 100)+ " %" )
