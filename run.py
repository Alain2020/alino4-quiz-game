#------------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in quuestions:
        print("--------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
         guess = input("Enter (A, B, C, or D): ")
         guess = guess.upper()
         guesses.append(guess)

         correct_guesse += check_answer(questions.get(key),guss)
    question_num += 1


#------------------------------
def check_answer(answer, guess):
    
     if answer == guess:
        print("COORECT!")
        return 1
        else:("WRONG!")
        return 0
#------------------------------
def display_score():
    pass
#------------------------------
def play_again():
    pass
#------------------------------

questions = {"What’s the fastest land animal in the world?: ": "A",
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

options   = [["A. The cheetah", "B. Lion", "C. Kangaroo", "D. Hyena "],
            ["A. One", "B. Nine", "C.Three", "D. Five "],
            ["A. Brazil", "B. United States", "C. Spain", "D.Uruguay "],
            ["A. Black", "B. Purple", "C. Pink", "D. Grey "],
            ["A. New York Knicks", "B. Orlando Magic", "C. Washington Wizards", "D. Chicago Bulls "],
            ["A. China", "B. The USA", "C. The UK", "D. Australia "],
            ["A. 1901", "B. 1921", "C. 1931", "D. 1911 "],
            ["A. Anthony Eden", "B. Robert Peel", "C. Bonar Law", "D. Gordon Brown "],
            ["A. Kenya", "B. Ethiopia", "C. Comoros", "D. Uganda "],
            ["A. Mozambique", "B. Namibia", "C. Tanzania", "D. Botswana "]]
