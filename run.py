#alino4 General knowledge Quiz Game

questions = ("What’s the fastest land animal in the world?: ",
             "How many hearts does an octopus have?: ",
             "What country won the very first FIFA World Cup in 1930?: ",
             "What color is the tongue of a giraffe?: ",
             "For which team did Michael Jordan spend most of his career playing?: ",
             "Which country has the most Olympic gold medals in swimming?: ",
             "What year did boxing become a legal sport?: ",
             "Who was Prime Minister of Great Britain from 1841 to 1846?: ",
             "Name the East African country which lies on the Equator?: ",
             "Which country is the island of Zanzibar part of?: ")

options   = (("A. The cheetah", "B. Lion", "C. Kangaroo", "D. Hyena "),
            ("A. One", "B. Nine", "C.Three", "D. Five "),
            ("A. Brazil", "B. United States", "C. Spain", "D.Uruguay "),
            ("A. Black", "B. Purple", "C. Pink", "D. Grey "),
            ("A. New York Knicks", "B. Orlando Magic", "C. Washington Wizards", "D. Chicago Bulls "),
            ("A. China", "B. The USA", "C. The UK", "D. Australia "),
            ("A. 1901", "B. 1921", "C. 1931", "D. 1911 "),
            ("A. Anthony Eden", "B. Robert Peel", "C. Bonar Law", "D. Gordon Brown "),
            ("A. Kenya", "B. Ethiopia", "C. Comoros", "D. Uganda "),
            ("A. Mozambique", "B. Namibia", "C. Tanzania", "D. Botswana "))

answers = ("A", "C", "D", "B", "D", "B", "A", "B", "A", "C",)
guesses = []
score = 0

question_num = 0 

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)