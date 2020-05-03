import numpy as np
import itertools


def string_matcher(str1, str2, ratio_calc='False'):
    str1 = str1.lower()
    str2 = str2.lower()

    rows = len(str1) + 1
    cols = len(str2) + 1

    distance = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            if str1[row - 1] == str2[col - 1]:
                cost = 0
            else:
                if ratio_calc:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of deletions
                                     distance[row][col - 1] + 1,  # Cost of insertions
                                     distance[row - 1][col - 1] + cost)  # Cost of substitution
    if ratio_calc:
        ratio = ((len(str1) + len(str2)) - distance[row][col]) / (len(str1) + len(str2))
        return ratio
    else:
        return "The strings are {} edits away".format(distance[row][col])


def get_close_matches(str, data, n=9, cutoff=0.60):
    close_word = [""] * (n + 1)
    ratio_word = [cutoff] * (n + 1)
    for word in data:
        word_ratio = string_matcher(str, word)
        for i in range(n):
            if ratio_word[i] < word_ratio:
                ratio_word[i + 1] = ratio_word[i]
                close_word[i + 1] = close_word[i]
                ratio_word[i] = word_ratio
                close_word[i] = word
                break
    return close_word
