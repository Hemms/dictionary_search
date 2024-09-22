import json
import difflib


def load_data():
    with open("data.json") as file:
        data = json.load(file)
    return data


# function to get the word defination
def get_defination(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return None


# function to suggest similar words
def get_suggestions(word, dictionary):
    matches = difflib.get_close_matches(word, dictionary.keys(), n=1)
    if matches:
        return matches[0]
    else:
        return None


# Main function to run the program
def run_program():
    dictionary = load_data()
    word = input("Enter a word: ")

    # Get a defination
    defination = get_defination(word, dictionary)

    if defination:
        print(f"Defination of '{word}': {defination}")

    else:
        suggestion = get_suggestions(word, dictionary)
        if suggestion:
            print(f"Word Not Found. Did you mean '{suggestion}'?")
        else:
            print("Word not found, and no suggestions available.")


if __name__ == "__main__":
    run_program()
