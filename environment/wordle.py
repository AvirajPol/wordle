from random import choice


def reset():
    result = list(choose_word())

    game = {
        "result": result,
        "attempt": 0,
        "guesses": [],
        "feedback": [],
        "state": 0
    }

    return game


def game_state(state):
    if state == 1:
        print("Congratulations! You've guessed the word correctly!")
        print("Thanks for playing Wordle!")

    elif state == 2:
        print("Game over! You used all 6 attempts.")

    else:
        print("Welcome to Wordle!")
        print("You have 6 tries to guess the 5-letter word.")
        print("After each guess, you will receive feedback:")
        print("Green: Correct letter in the correct position.")
        print("Yellow: Correct letter in the wrong position.")
        print("Grey: Incorrect letter.")
        print("Type 'exit' to quit the game at any time.")


def choose_word():
    words = []
    with open("data/words/words.txt", "r") as file:
        for word in file:
            words.append(word.strip())
    return choice(words)


def step(game, guess):

    result = game["result"]
    input_val = list(guess)

    hashmap = {}

    for char in result:
        hashmap[char] = hashmap.get(char, 0) + 1

    arr1 = ["grey"] * 5

    # First pass: Green letters
    for i in range(5):
        if input_val[i] == result[i]:
            arr1[i] = "green"
            hashmap[input_val[i]] -= 1

    # Second pass: Yellow letters
    for i in range(5):
        if arr1[i] != "green" and hashmap.get(input_val[i], 0) > 0:
            arr1[i] = "yellow"
            hashmap[input_val[i]] -= 1

    game["attempt"] += 1

    game["guesses"].append(guess)
    game["feedback"].append(arr1.copy())

    # Update game status
    if input_val == result:
        game["state"] = 1

    elif game["attempt"] == 6:
        game["state"] = 2

    return arr1, game["state"]


def input_value():
    return input("Enter your 5-letter word: ").strip().lower()


def main():

    game = reset()

    game_state(0)

    while game["attempt"] < 6 and game["state"] == 0:

        val = input_value()

        if val == "exit":
            print("Thanks for playing!")
            return

        if len(val) != 5 or not val.isalpha():
            print("Please enter exactly 5 letters.")
            continue

        feedback, state = step(game, val)

        print("Input:", val)
        print("Attempt:", game["attempt"])
        print("Feedback:", feedback)

        if state != 0:
            game_state(state)

            if state == 2:
                print("The correct word was:", "".join(game["result"]))


if __name__ == "__main__":
    main()