# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("If you get a question right, you score ammount earned goes up 1\n")
    print("\t\t", title, "\n")
 
def main():
    global score
    newscore = 1
    trivia_file = open_file("trivia2.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += newscore
            newscore += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    
    
main()

player1 = input("What is your name? ")
final = (player1, score)

try:
    highscores = pickle.load(open("highscores.txt", "rb"))
except:
    highscores = []

highscores.append(final)
highscores = sorted(highscores, key=lambda tup: tup[1], reverse=True)
if len(highscores) > 5:
    highscores.pop()

pickle.dump(highscores, open("highscores.txt", "wb"))

print("\tHighscores: ")
for i in highscores:
    num = i[1]
    print(i[0] + " - " + str(num))
            
input("\n\nPress the enter key to exit.")
