#%%
import random

file = 'C:/Users/hp/Desktop/Work/Millionire questions.txt'
fileReader = open(file)
questions = fileReader.read().split("|\n")
random.shuffle(questions)
def million():
    answerkey = {"DotA": "A", "sphinx": "A", "animals": "C", "term": "D",
                 "Pokemon?": "B", "Norse": "C", "Tekken": "A", "monarcy": "C",
                 "Key":"D", "Nintendo":"B"}
    x = 0
    y = 0
    while True:
        if(x < 4):
            print(questions[y])
            for keys in answerkey:
                if keys in questions[y]:
                    correct = answerkey[keys]
            answer = input("Choose A, B, C or D")
            #\n or type 50 for 50/50: 
            if (answer.upper() == correct):
                x += 1
                y += 1
                print("Correct!, Next question!\n")
            #elif (str(answer) == "50"):
                #answer = input(correct, "or", )
            #elif answer != "A" and answer != "B" and answer != "C" and answer "D":
            else:
                print("Too bad, wrong answer")
                return False
        else:
            print("You Win!")
            return False
million()
                
            