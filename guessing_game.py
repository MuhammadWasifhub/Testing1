from spellchecker import SpellChecker

def check_english(text):
    """Checks for spelling and basic grammatical errors in a given text."""
    spell = SpellChecker()
    words = text.lower().split()
    misspelled = spell.unknown(words)
    errors = []

    # Check for spelling mistakes
    for word in misspelled:
        corrected_word = spell.correction(word)
        if corrected_word:
            errors.append(f'In your sentence "{word}" is incorrect, the corrected one is "{corrected_word}".')
        else:
            errors.append(f'In your sentence "{word}" is incorrect and no correction was found.')

    # Basic check for repeated words
    for i in range(len(words) - 1):
        if words[i] == words[i+1]:
            errors.append(f'In your sentence, the word "{words[i]}" is repeated consecutively.')

    return errors

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter anything (or type 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break

            detected_errors = check_english(user_input)

            if detected_errors:
                print("Detected errors:")
                for error in detected_errors:
                    print(f"- {error}")
            else:
                print("No obvious spelling or grammatical errors detected.")
            print("\n")
        except EOFError:
            print("\nInput stream closed unexpectedly. Exiting.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
