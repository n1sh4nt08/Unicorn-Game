import pandas as pd
import random

# Load the Excel file
df = pd.read_excel('unicorns.xlsx')

def get_random_question():
    row = df.sample(n=1).iloc[0]
    return row['Attribute'], row['Startup']

def play_game():
    score = 0
    while True:
        attribute, startup = get_random_question()
        print(f"Guess the startup based on this attribute: {attribute}")
        guess = input("Your guess: ")
        if guess.lower() == startup.lower():
            score += 1
            print(f"Correct! Your score is {score}.")
        else:
            print(f"Wrong! The correct answer was {startup}.")
            print(f"Your final score is {score}.")
            break
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()

if __name__ == "__main__":
    play_game()
