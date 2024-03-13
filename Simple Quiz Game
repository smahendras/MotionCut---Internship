def new_game():
    guesses=[]
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("------------")
        print(key)

        for i in options[question_num-1]:
            print(i)
        guess = input("Choose one option: ")
        #guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)


def check_answer(answer,guess):
    if answer == guess:
        print("....correct....")
        return 1
    else :
        print("wrong answer!!!")

        return 0


def display_score(correct_guesses,guesses):
    print("----------------------")
    print("Result")
    print("----------------------")
    print("Answers: ", end="")
    for i in question:
        print(question.get(i),end="")
    print()

    print("Guesses :",end="")
    for i in guesses:
        print(i,end="")
    print()

    score =int((correct_guesses/len(question))*100)
    print("your score is : "+str(score)+"%")



def play_again():
    response = input("Do you want to play again? (Yes/No): ")
    #response = response.upper()

    if response =="Yes":
        return True
    else:
        return False


question = {
    "1.A train, 150 m long, takes 30 seconds to cross a bridge 500 m long. How much time will the train take to cross a platform 370 m long ?: ":"c",
    "2.If a man running at 15 kmph crosses a bridge in 5 minutes, the length of the bridge is ?: ":"d",
    "3.In which ocean is the Island country Fiji situated ?: ": "d",
    "4.The rhythmic rise and fall of ocean water twice in a day is called ______ ?: ":"b",
    "5.Antonym - Enigma ?":"d"
}

options=[
    ["a. 36 secs" ,"b. 30 secs" , "c. 24 secs" ,"d. 18 secs"],
    ["a. 1000 metres" ,"b. 500 metres ","c. 750 metres " , "d.1250 metres"],
    ["a.Indian Ocean ", "b. Arctic Ocean ","c. Atlantic Ocean ","d. Pacific ocean"],
    ["a.Wave" ,"b.Tide ","c.Tsunami" ,"d.Current"],
    ["a.Mystery" ,"b.Charade ","c.Make-believe ","d.Clarity "]
]
#correct_answer=[[1.'C'],[2.'D'],[3.'D'],[4.'B'],[5.'D']]

new_game()

while play_again():
    new_game()

print("Byee!!!")
