"""
CP1404/CP5632 - Practical
Scores
"""
import random

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    user_score = float(input("Enter your score: "))
    result = determine_result(user_score)
    print(result)

    random_score = random.randint(0, 100)
    result = determine_result(random_score)
    print(f"Random score ({random_score}): {result}")

main()
