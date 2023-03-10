import time

# ----------------- Welocme the user
print("Welcome to the Solino Quiz Game! ")
time.sleep(1)
#---------------
playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    time.sleep(1)
print("Okay! let's play! :)")
time.sleep(1)

#-----------------

#chances 
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in QUESTIONS:
        print("-------------------------")
        print(key)
        for i in OPTIONS[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(QUESTIONS.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT! Good Job.\n")
        time.sleep(2)
        return 1

    else:
        print("WRONG!\n ")
        time.sleep(0.5)
        return 0
        

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in QUESTIONS:
        print(QUESTIONS.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(QUESTIONS))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


QUESTIONS = {"What’s the fastest land animal in the world?: ": "A",
             "How many hearts does an octopus have?: ": "C",
             "What country won the very first FIFA World Cup in 1930?: ": "D",
             "What color is the tongue of a giraffe?: ": "B",
             "For which team did Michael Jordan spend most of his career playing?: " : "D",
             "Which country has the most Olympic gold medals in swimming?: " : "B",
             "What year did boxing become a legal sport?: " : "A",
             "Who was Prime Minister of Great Britain from 1841 to 1846?: " : "B",
             "Name the East African country which lies on the Equator?: " : "A",
             "Which country is the island of Zanzibar part of?: " : "C"
             }

OPTIONS   = [["A. The cheetah", "B. Lion", "C. Kangaroo", "D. Hyena "],
            ["A. One", "B. Nine", "C.Three", "D. Five "],
            ["A. Brazil", "B. United States", "C. Spain", "D.Uruguay "],
            ["A. Black", "B. Purple", "C. Pink", "D. Grey "],
            ["A. New York Knicks", "B. Orlando Magic", "C. Washington Wizards", "D. Chicago Bulls "],
            ["A. China", "B. The USA", "C. The UK", "D. Australia "],
            ["A. 1901", "B. 1921", "C. 1931", "D. 1911 "],
            ["A. Anthony Eden", "B. Robert Peel", "C. Bonar Law", "D. Gordon Brown "],
            ["A. Kenya", "B. Ethiopia", "C. Comoros", "D. Uganda "],
            ["A. Mozambique", "B. Namibia", "C. Tanzania", "D. Botswana "]]


new_game()

while play_again():
    new_game()

#Goodbye Message
print("Thank you for playing the Simple Quiz Game!")
print("Byeeeeee!")

# -------------------------