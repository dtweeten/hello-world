def wordle_game(secret_word):
    secret_word = secret_word.lower()
    attempts = 6

    print("Welcome to Wordle!")
    print("You have 6 attempts to guess the 5-letter word.")
    print("Feedback: 🟩 = correct letter & position, 🟨 = letter in word but wrong position, ⬜ = letter not in word\n")

    for attempt in range(attempts):
        while True:
            guess = input(f"Attempt {attempt + 1}/6 - Enter your 5-letter guess: ").lower()
            if len(guess) != 5 or not guess.isalpha():
                print("Please enter a valid 5-letter word.")
            else:
                break

        result = ""
        secret_word_chars = list(secret_word)  # For marking letters used

        # First pass: check greens
        result_chars = [""] * 5
        for i in range(5):
            if guess[i] == secret_word[i]:
                result_chars[i] = "🟩"
                secret_word_chars[i] = None  # Mark as used

        # Second pass: check yellows and grays
        for i in range(5):
            if result_chars[i] == "":
                if guess[i] in secret_word_chars:
                    result_chars[i] = "🟨"
                    secret_word_chars[secret_word_chars.index(guess[i])] = None
                else:
                    result_chars[i] = "⬜"

        print("".join(result_chars))

        if guess == secret_word:
            print("🎉 Congratulations! You guessed the word!")
            return

    print(f"Sorry, you're out of attempts! The word was: {secret_word}")

if __name__ == "__main__":
    secret = input("Set the secret 5-letter word: ").strip()
    while len(secret) != 5 or not secret.isalpha():
        secret = input("Invalid word. Please enter a 5-letter word: ").strip()

    print("\n" * 50)  # Clear screen to hide the secret word
    wordle_game(secret)

