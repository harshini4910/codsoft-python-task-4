import random
from collections import defaultdict

CHOICES = ["rock", "paper", "scissors"]
EMOJI = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}


pattern_memory = defaultdict(lambda: defaultdict(int))

def counter_move(move):
    return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[move]

def predict_next_move(last_move):
    if last_move and last_move in pattern_memory:
        next_moves = pattern_memory[last_move]
        if next_moves:
            return max(next_moves, key=next_moves.get)
    return random.choice(CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if wins[user] == computer else "computer"

def play_game():
    print("\n🤖 ROCK • PAPER • SCISSORS — AI BRAIN MODE 🤖")
    rounds = int(input("Enter number of rounds: "))

    user_score = computer_score = 0
    last_user_move = None

    for round_no in range(1, rounds + 1):
        print(f"\n🔹 Round {round_no}")
        user = input("Choose rock / paper / scissors: ").lower()

        if user not in CHOICES:
            print("❌ Invalid choice! Round skipped.")
            continue

      
        predicted_user_move = predict_next_move(last_user_move)
        computer = counter_move(predicted_user_move)

        print(f"You chose: {EMOJI[user]}")
        print(f"AI chose:  {EMOJI[computer]}")

        winner = determine_winner(user, computer)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "user":
            print("🎉 You outsmarted the AI!")
            user_score += 1
        else:
            print("🧠 AI predicted your move!")
            computer_score += 1

        print(f"Score ➜ You: {user_score} | AI: {computer_score}")

      
        if last_user_move:
            pattern_memory[last_user_move][user] += 1
        last_user_move = user

    print("\n📊 FINAL RESULT")
    print(f"You: {user_score} | AI: {computer_score}")

    if user_score > computer_score:
        print("🏆 HUMAN WINS!")
    elif user_score < computer_score:
        print("🤖 AI DOMINATES!")
    else:
        print("⚖️ DRAW MATCH!")

    print("\nThanks for challenging the AI 😈")

play_game()
