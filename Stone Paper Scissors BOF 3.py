import random

def get_player_choice():
    """Get and validate player's choice"""
    while True:
        choice = input("Your choice (stone/paper/scissors): ").lower()
        if choice in ['stone', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please enter stone, paper, or scissors.")

def determine_round_winner(p1_choice, c_choice):
    """Determine the winner of a single round"""
    if p1_choice == c_choice:
        return 'tie'
    winning_combinations = {
        'stone': 'scissors',
        'paper': 'stone',
        'scissors': 'paper'
    }
    if winning_combinations[p1_choice] == c_choice:
        return 'player'
    return 'computer'

def play_best_of_three():
    """Play a best-of-three Stone-Paper-Scissors game"""
    player_score = 0
    computer_score = 0
    round_num = 1
    
    print("\n=== BEST OF THREE Stone-PAPER-SCISSORS ===")
    print("First to win 2 rounds wins the game!\n")
    
    while player_score < 2 and computer_score < 2:
        print(f"\n--- Round {round_num} ---")
        print(f"Score: You {player_score} - {computer_score} Computer")
        
        # Get choices
        player_choice = get_player_choice()
        computer_choice = random.choice(['stone', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        result = determine_round_winner(player_choice, computer_choice)
        
        if result == 'player':
            player_score += 1
            print("You win this round!")
        elif result == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        round_num += 1
    
    # Determine overall winner
    print("\n=== FINAL RESULT ===")
    print(f"Final Score: You {player_score} - {computer_score} Computer")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("Computer won the game. Better luck next time!")

#Ask if they want to play.
Ans=input("Would you like to play a game called Stone Paper Scissors (Yes/No): ")

if Ans=="Yes":
    Name=input("Your Name?: ")
    age=int(input('Age?: '))

    print("To start first you have to give a try to your luck.")
    print("Computer will generate a random number from 1-100.")
    print("If number come out to be even you can continue otherwise you can not.")


    begin=str(input("Type Begin to continue: "))
    if begin=="Begin":
        randnum=random.randint(1,100)
        print(f"Random number by computer is {randnum}.")
        
        if randnum%2==0:
            print("Congrats number came out to be even.")
            play_best_of_three()
        else:
            print("Seems like luck is not on your side.")
else:
    print("No Issues.")