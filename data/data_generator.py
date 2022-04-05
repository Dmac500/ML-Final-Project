import csv


# import numpy as np


def score(guess_word, answer_word):
    """
    :param guess_word: The word that was guessed
    :param answer_word: The actual answer
    :return: A list of scores for each letter in the guess word
    """
    # Convert to lists
    guess_letters = []
    guess_letters[:0] = guess_word

    answer_letters = []
    answer_letters[:0] = answer_word

    # For each letter in the guess_word
    #   we assign a score
    scores = [0, 0, 0, 0, 0]

    # First: score the letters at the correct positions
    for i in range(0, 5):

        if guess_letters[i] == answer_letters[i]:
            scores[i] = 2
            guess_letters[i] = "*"
            answer_letters[i] = "#"

    # Second: score the letters at the wrong positions
    for i in range(0, 5):

        if guess_letters[i] == "*":
            continue

        if guess_letters[i] in answer_letters:
            guess_letter_freq = find_freq(guess_letters[i], guess_letters)
            answer_letter_freq = find_freq(guess_letters[i], answer_letters)
            if guess_letter_freq == answer_letter_freq:
                scores[i] = 1
            elif guess_letter_freq > answer_letter_freq:
                scores[i] = 1
                index_of_guess_letter_in_answer = answer_letters.index(guess_letters[i])
                answer_letters[index_of_guess_letter_in_answer] = "*"
            else:
                scores[i] = 1

    return scores


def find_freq(c, word):
    i = 0
    for letter in word:
        if letter == c:
            i = i + 1
    return i


def main():
    file = open("words.csv", "r")
    csv_reader = csv.reader(file)

    word_list = []
    for row in csv_reader:
        word_list.append(row[0])
    word_list = word_list[1:]

    print(word_list)


if __name__ == "__main__":
    main()
