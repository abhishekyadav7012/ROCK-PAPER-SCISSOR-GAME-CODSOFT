import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\n--- Final Score ---")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the series!")
    elif user_score < computer_score:
        print("The computer won the series. Better luck next time!")
    else:
        print("The series ended in a tie!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    print("You'll be playing against the computer.")
    play_game()