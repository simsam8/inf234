def hamming_distance(word1, word2):
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    distance += abs(len(word1) - len(word2))

    return distance


def levenshtein_distance_recursive(word1, word2):
    if len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)
    elif word1[0] == word2[0]:
        return levenshtein_distance_recursive(word1[1:], word2[1:])
    else:
        return 1 + min(
            levenshtein_distance_recursive(word1[1:], word2),  # delete from word1
            levenshtein_distance_recursive(word1, word2[1:]),  # insert into word1
            levenshtein_distance_recursive(
                word1[1:], word2[1:]
            ),  # replace character in word1
        )


def levenshtein_distance_dp(X, Y):
    OPT = {}
    lx = len(X)
    ly = len(Y)

    for i in range(lx + 1):
        for j in range(ly + 1):
            if i == 0 or j == 0:
                OPT[(i, j)] = max(i, j)
            elif X[i - 1] == Y[j - 1]:
                OPT[(i, j)] = OPT[(i - 1, j - 1)]
            else:
                OPT[(i, j)] = 1 + min(
                    OPT[(i - 1, j)], OPT[(i, j - 1)], OPT[(i - 1, j - 1)]
                )

    return OPT[(lx, ly)]
