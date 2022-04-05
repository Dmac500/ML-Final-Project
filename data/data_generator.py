import csv
import pandas as pd


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
    """
    :param c: a character
    :param word: a word
    :return: number of occurrences of c in word
    """
    i = 0
    for letter in word:
        if letter == c:
            i = i + 1
    return i


def sum_up_list(list_of_nums):
    """
    :param list_of_nums: A list of numbers
    :return: Summation of all the numbers in the list
    """
    summation = 0
    for num in list_of_nums:
        summation = summation + num
    return summation


def get_as_pandas_data_frame():
    """
    Reads from word.csv
    Scores each word against every other word and accumulates this data
    :return: The data is returned as a pandas dataframe of the following format:

                 guess actual  score
        0        aback  aback     10
        1        aback  abase      6
        2        aback  abate      6
        3        aback  abbey      4
        4        aback  abbot      4
        ...        ...    ...    ...
        5359220  zonal  young      3
        5359221  zonal  youth      2
        5359222  zonal  zebra      3
        5359223  zonal  zesty      2
        5359224  zonal  zonal     10
    """
    
    file = open("words.csv", "r")
    csv_reader = csv.reader(file)

    word_list = []
    for row in csv_reader:
        word_list.append(row[0])
    word_list = word_list[1:]

    data = []
    for guess_word in word_list:
        for answer_word in word_list:
            guess_score = sum_up_list(score(guess_word, answer_word))
            data.append([guess_word, answer_word, guess_score])

    df = pd.DataFrame(data, columns=["guess", "actual", "score"])

    return df


def main():
    file = open("words.csv", "r")
    csv_reader = csv.reader(file)

    word_list = []
    for row in csv_reader:
        word_list.append(row[0])
    word_list = word_list[1:]

    data = []
    for guess_word in word_list:
        for answer_word in word_list:
            guess_score = sum_up_list(score(guess_word, answer_word))
            data.append([guess_word, answer_word, guess_score])

    df = pd.DataFrame(data, columns=["guess", "actual", "score"])

    print(df)


if __name__ == "__main__":
    main()
