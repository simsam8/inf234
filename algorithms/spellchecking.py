def hamming_distance(word1, word2):
    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    distance += abs(len(word1) - len(word2))

    return distance


def leveshtein_distance(word1, word2):
    if len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)
    elif word1[0] == word2[0]:
        return leveshtein_distance(word1[1:], word2[1:])
    else:
        return 1 + min(
            leveshtein_distance(word1[1:], word2),  # delete from word1
            leveshtein_distance(word1, word2[1:]),  # insert into word1
            leveshtein_distance(word1[1:], word2[1:]),  # replace character in word1
        )
